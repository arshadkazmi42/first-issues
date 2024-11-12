# -*- coding: utf-8 -*-
from __future__ import print_function
import re
from datetime import datetime
import requests
import tweepy
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)


DAYS_OLD = 15
MAX_TWEETS_LEN = 280

ellipse = u'…'
api = 'https://api.github.com/search/issues'
FIRST_ISSUE_QUERY_URL = api + '?q=label:"{}"+is:issue+is:open&sort=updated&order=desc'

# Logging helper function
def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)


def humanize_url(api_url: str) -> str:
    """Make an API endpoint to a Human endpoint."""
    match = re.match(
        'https://api.github.com/repos/(.*)/(.*)/issues/([0-9]*)', api_url)
    if not match:
        raise ValueError(f'Format of API URLs has changed: {api_url}')
    user, repo, issue_num = match.group(1, 2, 3)

    return f'https://github.com/{user}/{repo}/issues/{issue_num}'


def get_first_timer_issues(issue_label: str) -> list:
    """Fetches the first page of issues with the label first-timers-label
    which are still open.
    """
    res = requests.get(FIRST_ISSUE_QUERY_URL.format(issue_label))
    res.raise_for_status()

    items = [item for item in res.json()['items']
            if check_days_passed(item['created_at'], DAYS_OLD)]

    return items


def check_days_passed(date_created: str, days: int) -> bool:
    created_at = datetime.strptime(date_created, "%Y-%m-%dT%H:%M:%SZ")
    return (datetime.now() - created_at).days < days


def add_repo_languages(issues):
    """Adds the repo languages to the issues list."""
    for issue in issues:
        query_languages = issue['repository_url'] + '/languages'
        res = requests.get(query_languages)
        if res.status_code == 403:
            log_warning('Rate limit reached getting languages')
            return issues
        if res.ok:
            issue['languages'] = res.json()
        else:
            log_warning('Could not handle response: ' +
                          str(res) + ' from the API.')
    return issues


def get_fresh(old_issue_list, new_issue_list):
    """Returns which issues are not present in the old list of issues."""
    old_urls = {x['url'] for x in old_issue_list}
    return [x for x in new_issue_list if x['url'] not in old_urls]


def tweet_issues(issues, creds, debug=False):
    """Takes a list of issues and credentials and tweets through the account
    associated with the credentials.
    Also takes a parameter 'debug', which can prevent actual tweeting.
    Returns a list of tweets.
    """
    if len(issues) == 0:
        return []

    auth = tweepy.OAuthHandler(creds['Consumer Key'], creds['Consumer Secret'])
    auth.set_access_token(creds['Access Token'], creds['Access Token Secret'])
    api = tweepy.API(auth)

    # This results in an API call to /help/configuration
    # conf = api.configuration()

    # url_len = conf['short_url_length_https']
    url_len = 30
    hashTags = u"#github"

    # 1 space with URL and 1 space before hashtags.
    allowed_title_len = MAX_TWEETS_LEN - (url_len + 1) - (len(hashTags) + 1)

    tweets = []

    for issue in issues:
        # Not encoding here because Twitter treats code points as 1 character.
        language_hashTags = ''
        title = issue['title']

        if len(title) > allowed_title_len:
            title = title[: allowed_title_len - 1] + ellipse
        else:
            if 'languages' in issue:
                language_hashTags = ''.join(
                    ' #{}'.format(lang) for lang in issue['languages']
                )
                hashTags = hashTags + language_hashTags

            max_hashtags_len = MAX_TWEETS_LEN - \
                (url_len + 1) - (len(title) + 1)

            if len(hashTags) > max_hashtags_len:
                hashTags = hashTags[:max_hashtags_len - 1] + ellipse

        url = humanize_url(issue['url'])

        try:
            # Encoding here because .format will fail with Unicode characters.
            tweet = '{title} {url} {tags}'.format(
                title=title,
                url=url,
                tags=hashTags
            )

            if not debug:
                api.update_status(tweet)

            tweets.append({
                'error': None,
                'tweet': tweet
            })

            log_info('Tweeted issue: {}'.format(issue['title']))
        except Exception as e:
            tweets.append({
                'error': e,
                'tweet': tweet
            })

            log_error('Error tweeting issue: {}'.format(issue['title']))
            log_error('Error message: {}'.format(str(e)))

    return tweets


def limit_issues(issues, limit_len=100000):
    """Limit the number of issues saved in our DB."""
    sorted_issues = sorted(issues, key=lambda x: x['updated_at'], reverse=True)
    return sorted_issues[:limit_len]
