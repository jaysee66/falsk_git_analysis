import git
import matplotlib.pyplot as plt
import pandas as pd

import git

def get_git_commits(repo_path):
    # 打开 Git 仓库
    repo = git.Repo(repo_path)
    # 获取所有的提交记录
    commits = list(repo.iter_commits('master'))  # 'master' 可以换成你自己的分支名
    # 提取需要的信息：作者、提交时间、提交信息
    commit_data = [{'author': commit.author, 'date': commit.committed_datetime, 'message': commit.message} for commit in commits]
    return commit_data
