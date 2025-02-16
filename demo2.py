import os
import csv
from git import Repo

def get_commit_history(repo_path):
    print(f"正在加载仓库: {repo_path}")
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())
    commit_history = []

    for commit in commits:
        commit_info = {
            "commit_id": commit.hexsha,
            "author": commit.author.name,
            "email": commit.author.email,
            "date": commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "message": commit.message.strip(),
            "files_changed": commit.stats.total["files"],
            "insertions": commit.stats.total["insertions"],
            "deletions": commit.stats.total["deletions"],
        }
        commit_history.append(commit_info)
        print(f"提取提交: {commit_info['commit_id']}")

    return commit_history

def save_to_csv(commit_history, output_file):
    print(f"正在保存提交历史到文件: {output_file}")
    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "commit_id",
            "author",
            "email",
            "date",
            "message",
            "files_changed",
            "insertions",
            "deletions",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for commit in commit_history:
            writer.writerow(commit)
    print(f"提交历史记录已保存到 {output_file}")


# 示例：处理本地 Git 仓库并保存到 CSV 文件
repo_path = r"C:\Users\93718\Desktop\flask-repo"  # 本地 Git 仓库路径
output_csv = r"C:\Users\93718\Desktop\flask_commits.csv"  # 输出的 CSV 文件路径

# 获取提交历史记录
commit_history = get_commit_history(repo_path)

# 保存为 CSV 文件
save_to_csv(commit_history, output_csv)