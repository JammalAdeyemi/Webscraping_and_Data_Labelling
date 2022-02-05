from github import Github
import pandas as pd

access_token = "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"

project_list = ['apache/any23', 'apache/dubbo', 'apache/calcite', 'apache/cassandra', 'apache/cxf',
                'apache/flume', 'apache/groovy']



def extract_user():
    df_project = pd.DataFrame()

    for project in project_list:
        g = Github(access_token)
        user = g.get_user().search_repositories("topic:machine-learning")
        #users = g.search_repositories("topic:machine-learning")

        df_project = df_project.append({
            'User_ID': user.id,
            'UserName': user.username,
            'Full_name': user.full_name,
            'Bio' : user.bio,
            'Blog': user.blog,
            'Company': user.organization,
            'Email': user.email,
            'Followers': user.followers_count,
            'Following': user.following_count,
            'url' : user.url,
            'location': user.location,
            # 'Forks': repo.forks_count,
            # 'Stars': repo.stargazers_count,
        }, ignore_index=True)
    df_project.to_csv('../Dataset/project_dataset.csv', sep=',', encoding='utf-8', index=True)

extract_user()
    