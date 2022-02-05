from github import Github
import pandas as pd
import requests
import time

project_list = ['apache/any23', 'apache/dubbo', 'apache/calcite', 'apache/cassandra', 'apache/cxf',
                'apache/flume', 'apache/groovy']

access_token = "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"

def extract_project_info():
    df_project = pd.DataFrame()

    for project in project_list:
        g = Github(access_token)
        repo = g.get_repo(project)
        PRs = repo.get_pulls(state='all')
        df_project = df_project.append({
            'Project_ID': repo.id,
            'Name': repo.name,
            'Full_name': repo.full_name,
            'Language': repo.language,
            'Forks': repo.forks_count,
            'Stars': repo.stargazers_count,
            'Watchers': repo.subscribers_count,
            'PRs_count': PRs.totalCount
        }, ignore_index=True)
    df_project.to_csv('../Dataset/project_dataset.csv', sep=',', encoding='utf-8', index=True)

extract_project_info()