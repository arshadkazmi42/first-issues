
def filter_issues(issues, label="good-first-issue"):
    """Filter issues by label."""
    return [issue for issue in issues if label in issue.get("labels", [])]

if __name__ == "__main__":
    print("Issue filter module loaded.")