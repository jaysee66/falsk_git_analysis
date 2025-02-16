import unittest
from unittest.mock import patch, MagicMock
import csv
import os
from demo3 import get_commit_history, save_to_csv


class TestDemo2(unittest.TestCase):

    @patch('git.Repo')
    def test_get_commit_history(self, MockRepo):
        """测试获取提交历史记录"""
        mock_repo = MagicMock()
        MockRepo.return_value = mock_repo
        mock_commits = [MagicMock(hexsha='1234567890', author='John Doe', message='Initial commit',
                                  committed_datetime='2021-01-01')]
        mock_repo.iter_commits.return_value = mock_commits

        repo_path = "D:/path_to_repo"
        commit_history = get_commit_history(repo_path)

        # 断言 commit_history 中的提交数量
        self.assertEqual(len(commit_history), 1)
        self.assertEqual(commit_history[0]['commit_id'], '1234567890')

    @patch('csv.DictWriter')
    def test_save_to_csv(self, MockDictWriter):
        """测试保存提交历史到 CSV 文件"""
        mock_writer = MagicMock()
        MockDictWriter.return_value = mock_writer

        commit_history = [{"commit_id": "1234567890", "author": "John Doe", "message": "Initial commit"}]
        output_file = "D:/path_to_output.csv"

        save_to_csv(commit_history, output_file)

        # 验证是否调用了写入文件操作
        mock_writer.writeheader.assert_called_once()
        mock_writer.writerow.assert_called_once_with(
            {"commit_id": "1234567890", "author": "John Doe", "message": "Initial commit"})


if __name__ == '__main__':
    unittest.main()

