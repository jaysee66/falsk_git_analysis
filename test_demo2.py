import unittest
import os
import csv
from git import Repo
from demo2 import get_commit_history, save_to_csv
a

class TestGitCommitAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建一个临时 Git 仓库
        cls.test_repo_path = "./test_repo"
        if os.path.exists(cls.test_repo_path):
            os.system(f"rm -rf {cls.test_repo_path}")
        cls.repo = Repo.init(cls.test_repo_path)

        # 创建一个测试文件并提交
        test_file = os.path.join(cls.test_repo_path, "test.txt")
        with open(test_file, "w") as f:
            f.write("Hello, Git!")

        cls.repo.index.add([test_file])
        cls.repo.index.commit("Initial commit")

    def test_get_commit_history(self):
        commit_history = get_commit_history(self.test_repo_path)
        self.assertIsInstance(commit_history, list)
        self.assertGreater(len(commit_history), 0)
        self.assertIn("commit_id", commit_history[0])
        self.assertIn("author", commit_history[0])
        self.assertIn("message", commit_history[0])

    def test_save_to_csv(self):
        test_csv_file = "test_commits.csv"
        commit_history = get_commit_history(self.test_repo_path)
        save_to_csv(commit_history, test_csv_file)

        self.assertTrue(os.path.exists(test_csv_file))

        with open(test_csv_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), len(commit_history))
            self.assertEqual(rows[0]["commit_id"], commit_history[0]["commit_id"])

        os.remove(test_csv_file)

    @classmethod
    def tearDownClass(cls):
        os.system(f"rm -rf {cls.test_repo_path}")


if __name__ == "__main__":
    unittest.main()
