import unittest
import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from scripts.stat_check import check_device_status

class TestStatCheck(unittest.TestCase):
    def test_check_device_status(self):
        result = check_device_status("washing machine")
        self.assertEqual(result, "Status check for washing machine: All systems operational.")

if __name__ == "__main__":
    unittest.main()

