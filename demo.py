from git import Repo
import os

def get_remote_commit_history(repo_url, local_path):
    # 如果本地路径已存在，先删除
    if os.path.exists(local_path):
        print(f"本地路径 {local_path} 已存在，将被删除并重新克隆...")
        os.system(f"del -rf {local_path}")

    # 克隆远程仓库到本地
    print(f"正在克隆远程仓库 {repo_url} 到本地路径 {local_path}...")
    repo = Repo.clone_from(repo_url, local_path)
    print("克隆完成！")

    # 获取提交历史记录
    commits = list(repo.iter_commits())
    commit_history = []

    for commit in commits:
        commit_info = {
            "hash": commit.hexsha,
            "author": commit.author.name,
            "email": commit.author.email,
            "date": commit.committed_datetime,
            "message": commit.message.strip()
        }
        commit_history.append(commit_info)

    return commit_history

# 示例：获取 Flask 项目的提交历史记录
repo_url = "https://github.com/pallets/flask.git"  # Flask 项目的远程仓库 URL
local_path = "C:/Users/93718/Desktop/tmp/flask-repo"  # 本地临时路径
commit_history = get_remote_commit_history(repo_url, local_path)

# 打印提交历史记录
for commit in commit_history:
    print(commit)