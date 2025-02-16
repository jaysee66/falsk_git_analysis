import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
from demo4 import load_csv, clean_data, analyze_data, visualize_data


class TestDemo3(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_load_csv(self, mock_read_csv):
        """测试加载 CSV 文件"""
        mock_df = pd.DataFrame({'commit_id': ['12345'], 'author': ['John Doe']})
        mock_read_csv.return_value = mock_df

        file_path = "D:/path_to_file.csv"
        df = load_csv(file_path)

        # 断言数据框是否正确加载
        self.assertEqual(len(df), 1)
        self.assertEqual(df['author'][0], 'John Doe')

    def test_clean_data(self):
        """测试数据清洗"""
        data = {'commit_id': ['12345'], 'author': ['John Doe'], 'date': ['2021-01-01']}
        df = pd.DataFrame(data)

        cleaned_df = clean_data(df)

        # 断言日期列是否被正确转换为 datetime 类型
        self.assertTrue(pd.to_datetime(cleaned_df['date']).equals(cleaned_df['date']))

    def test_analyze_data(self):
        """测试数据分析"""
        data = {'author': ['John Doe', 'Jane Doe'], 'insertions': [10, 20], 'deletions': [5, 10]}
        df = pd.DataFrame(data)

        author_counts, daily_commits, author_stats = analyze_data(df)

        # 断言作者提交统计
        self.assertEqual(author_counts['John Doe'], 1)
        self.assertEqual(author_stats['insertions']['John Doe'], 10)

    @patch('matplotlib.pyplot.show')
    def test_visualize_data(self, mock_show):
        """测试数据可视化"""
        author_counts = pd.Series({'John Doe': 5})
        daily_commits = pd.Series([1, 2, 3])

        visualize_data(author_counts, daily_commits)

        # 验证是否调用了可视化绘图方法
        mock_show.assert_called()


if __name__ == '__main__':
    unittest.main()
