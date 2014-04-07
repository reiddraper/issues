from github import Github

def milestone_by_name(repo, milestone_name):
    milestones = list(repo.get_milestones())
    for m in milestones:
        if m.title == milestone_name:
            return m
    return None

def open_issues_in_milestone(repo, milestone):
    return repo.get_issues(milestone=milestone, state='open')

def open_issues_by_labels(repo, labels):
    return repo.get_issues(state='open', labels = labels)

def closed_issues_by_labels(repo, labels):
    return repo.get_issues(state='closed', labels = labels)
