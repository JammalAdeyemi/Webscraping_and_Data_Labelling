from github import Github

access_token = "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"

g = Github(access_token)

current_user = g.get_user()

# print(current_user.name)
# print(current_user.bio)

# Extract my personal respository
repos = g.get_user().get_repos()

# for repo in repos:
#     print(repo.name)

js_repos = g.search_repositories(query="language:java")
for repo in js_repos:
    print(repo)
    break