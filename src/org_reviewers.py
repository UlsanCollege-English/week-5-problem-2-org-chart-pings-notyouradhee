
## Starter code — `src/org_reviewers.py`

def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """
    # TODO: implement recursively
    if not root:
        return 0

    count = 1 if root.get("level", 0) >= min_level else 0

    for report in root.get("reports", []):
        count += count_senior(report, min_level)

    return count
