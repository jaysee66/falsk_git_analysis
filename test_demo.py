import unittest
from unittest.mock import patch, MagicMock
import os
from demo import get_remote_commit_history


class TestDemo1(unittest.TestCase):

    @patch('git.Repo.clone_from')
    def test_get_remote_commit_history(self, mock_clone):
        """测试成功克隆远程仓库"""
        # 模拟远程仓库的 URL 和本地路径
        repo_url = "https://github.com/pallets/flask.git"
        local_path = "D:/path_to_repo"

        # 模拟克隆操作
        mock_repo = MagicMock()
        mock_clone.return_value = mock_repo

        # 执行函数
        get_remote_commit_history(repo_url, local_path)

        # 验证是否调用了 clone_from 方法
        mock_clone.assert_called_once_with(repo_url, local_path)

    @patch('os.path.exists')
    @patch('git.Repo.clone_from')
    def test_existing_local_path(self, mock_clone, mock_exists):
        """测试本地路径已存在的情况"""
        mock_exists.return_value = True  # 模拟本地路径存在

        repo_url = "https://github.com/pallets/flask.git"
        local_path = "D:/path_to_repo"

        # 执行函数
        get_remote_commit_history(repo_url, local_path)

        # 验证是否执行了删除操作
        print(f"本地路径 {local_path} 已存在，将被删除并重新克隆...")
        mock_clone.assert_called_once_with(repo_url, local_path)


if __name__ == '__main__':
    unittest.main()
