import unittest
import os
from Repo_path import RepoPath


class TestRepoPath(unittest.TestCase):
    def test_folder_or_url_with_local_path(self):
        """Check if local return folder is correct"""
        existing_path = os.path.expanduser("~/")
        repo = RepoPath(existing_path)
        self.assertEqual(repo.folder_or_url(), existing_path)

    def test_folder_or_url_with_invalid_path(self):
        """Check if invalid folder path returns 'Error'"""
        invalid_path = "/NoWhere/Path"
        repo = RepoPath(invalid_path)
        self.assertEqual(repo.folder_or_url(), "Error")


if __name__ == "__main__":
    unittest.main()
