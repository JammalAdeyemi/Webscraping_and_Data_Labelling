from github import Github
from top_github_scraper import (get_top_repo_urls, get_top_repos ,get_top_contributors, get_top_user_urls, get_top_users)
import datapane as dp
import pandas as pd
import base64

project_list = ['apache/any23', 'apache/dubbo', 'apache/calcite', 'apache/cassandra', 'apache/cxf',
                'apache/flume', 'apache/groovy']

access_token = "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"

g = Github(access_token)

def print_repo(repo):
    # # repository full name
    # print("Full name:", repo.full_name)
    # # repository description
    # print("Description:", repo.description)
    # # the date of when the repo was created
    # print("Date created:", repo.created_at)
    # # the date of the last git push
    # print("Date of last push:", repo.pushed_at)
    # # home website (if available)
    # print("Home Page:", repo.homepage)
    # # programming language
    # print("Language:", repo.language)
    # # number of forks
    # print("Number of forks:", repo.forks)
    # # number of stars
    # print("Number of stars:", repo.stargazers_count)
    # print("-"*50)
    # # repository content (files & directories)
    # print("Contents:")
    print("Repo", repo)
    # for content in repo.get_contents(""):
    #     print(content)
    # try:
    #     # repo license
    #     print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    # except:
    #     pass
print()
for i, repo in enumerate(g.search_repositories("topic:machine-learning")):
    print_repo(repo)
    print("="*100)
    if i == 9:
        break
#df_project.to_csv('../Dataset/project_dataset.csv', sep=',', encoding='utf-8', index=True)
# def extract_users():
#     df_project = pd.DataFrame
#     for project in project_list:
#         g = Github(access_token)
#         keyward = g.search_topics(keyward)
#         repo = g.get_repo(project)
#         organization = g.get_organization()
#         PRs = repo.get_pulls(state='all')

#         df_project = df_project.append({
#             'User_ID': keyward.id,
#             'UserName': keyward.username,
#             'Full_name': keyward.full_name,
#             'Bio' : keyward.bio,
#             'Blog': keyward.blog,
#             'Company': organization.company,
#             'Email': keyward.email,
#             'Followers': keyward.followers_count,
#             'Following': keyward.following_count,
#             'url' : keyward.url,
#             'location': keyward.location,
#             'Forks': repo.forks_count,
#             'Stars': repo.stargazers_count,
#         }, ignore_index=True)
#     df_project.to_csv('project_dataset.csv', sep=',', encoding='utf-8', index=True)

# extract_users()

        