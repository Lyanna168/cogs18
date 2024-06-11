import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from scripts.allocation import allocate_resources
from my_module.classes import User

import unittest
from scripts.allocation import allocate_resources
from my_module.classes import User

class TestAllocation(unittest.TestCase):
    def test_allocate_resources(self):
        user = User("Alice")
        user.add_device("washing machine", "LG1234", 2018)
        result = allocate_resources(user, "washing machine")
        self.assertEqual(result, "Resources allocated for Alice's washing machine repair.")

if __name__ == "__main__":
    unittest.main()
