# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import warnings

import requests
import tweepy

ellipse = u'…'
query_string = 'https://api.github.com/search/issues?q=label:{}+is:issue+is:open&sort=updated&order=desc'
queries = [query_string.format('good-first-issue'), query_string.format('good first issue')]


def humanize_url(api_url):
    """Make an API endpoint to an Human endpoint."""
    match = re.match('https://api.github.com/repos/(.*)/(.*)/issues/([0-9]*)', api_url)
    if match is None:
        raise RuntimeError('Format of API URLs has changed: ', api_url)

    user, repo, issue_num = match.group(1), match.group(2), match.group(3)
    human_url_template = 'https://github.com/{user}/{repo}/issues/{issue_num}'

    return human_url_template.format(user=user, repo=repo, issue_num=issue_num)


def get_first_timer_issues():
    """Fetches the first page of issues with the label first-timers-label which are still open."""
    items = []
    for query in queries:
        res = requests.get(query)
        if res.status_code == 403:
            warnings.warn('Rate limit reached')
            return items
        elif res.ok:
            items.extend(res.json()['items'])
        else:
            raise RuntimeError('Could not handle response: ' + str(res) + ' from the API.')
    return items


def get_fresh(old_issue_list, new_issue_list):
    """Returns which issues are not present in the old list of issues."""
    old_urls = set(x['url'] for x in old_issue_list)
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
    conf = api.configuration()

    url_len = conf['short_url_length_https']
    hashTags = u'#github'
    # 1 space with URL and 1 space before hashtags.
    allowed_title_len = 140 - (url_len + 1) - (len(hashTags) + 1)

    tweets = []

    for issue in issues:
        # Not encoding here because Twitter treats code points as 1 character.
        title = issue['title']
        if len(title) > allowed_title_len:
            title = title[:allowed_title_len - 1] + ellipse

        url = humanize_url(issue['url'])

        try:
            # Encoding here because .format will fail with Unicode characters.
            tweet = '{title} {url} {tags}'.format(title=title.encode('utf-8'),
                                                  url=url.encode('utf-8'),
                                                  tags=hashTags.encode('utf-8'))

            if not debug:
                api.update_status(tweet)

            tweets.append({
                'error': None,
                'tweet': tweet
            })
        except Exception as e:
            tweets.append({
                'error': e,
                'tweet': tweet
            })

    return tweets


def limit_issues(issues, limit_len=100000):
    """Limit the number of issues saved in our DB."""
    sorted_issues = sorted(issues, key=lambda x: x['updated_at'], reverse=True)
    return sorted_issues[:limit_len]
