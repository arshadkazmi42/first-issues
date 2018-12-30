from first_timers import first_timers
import json

example_res = json.load(open('data/example.json', 'r'))
example_issues = example_res['items']


def test_fetcher():
    issue_list = first_timers.get_first_timer_issues()
    assert len(issue_list) > 0


test_fetcher.__setattr__('__test__', False)  # Test disabled by default.


def test_get_fresh():
    new_issues = first_timers.get_fresh(example_issues[:-1], example_issues)
    assert new_issues[0] == example_issues[-1]


def test_humanize_url():
    api_url = "https://api.github.com/repos/tidusjar/NZBDash/issues/53"
    human_url = 'https://github.com/tidusjar/NZBDash/issues/53'
    assert first_timers.humanize_url(api_url) == human_url
