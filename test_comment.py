import unittest
import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from scripts.comment import add_comment
from my_module.classes import User

class TestComment(unittest.TestCase):
    def test_add_comment(self):
        user = User("Alice")
        result = add_comment(user, "Thank you for the help!")
        self.assertEqual(result, "Comment added for Alice: Thank you for the help!")

if __name__ == "__main__":
    unittest.main()

