import unittest
from unittest.mock import patch, MagicMock
from demo1 import get_commit_history


class TestDemo1(unittest.TestCase):

    @patch('git.Repo')
    def test_get_commit_history(self, mock_repo):
        """测试获取 Git 提交历史"""

        # 模拟仓库路径
        repo_path = "D:/path_to_repo"

        # 模拟 Repo 实例
        mock_repo_instance = MagicMock()
        mock_repo.return_value = mock_repo_instance

        # 模拟返回的提交记录
        mock_commit = MagicMock()
        mock_commit.hexsha = 'abc123'
        mock_commit.author.name = 'John Doe'
        mock_commit.author.email = 'johndoe@example.com'
        mock_commit.committed_datetime.strftime.return_value = "2024-02-15 12:34:56"
        mock_commit.message = "Initial commit"
        mock_commit.stats.total = {"files": 1, "insertions": 10, "deletions": 2}

        # 模拟 Repo 实例的 iter_commits 返回一个提交列表
        mock_repo_instance.iter_commits.return_value = [mock_commit]

        # 执行函数
        commit_history = get_commit_history(repo_path)

        # 验证函数是否正确返回提交历史
        self.assertEqual(len(commit_history), 1)
        self.assertEqual(commit_history[0]["commit_id"], 'abc123')
        self.assertEqual(commit_history[0]["author"], 'John Doe')
        self.assertEqual(commit_history[0]["message"], 'Initial commit')


if __name__ == '__main__':
    unittest.main()
