import unittest
import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from scripts.player_menu import display_menu

class TestPlayerMenu(unittest.TestCase):
    def test_display_menu(self):
        menu = display_menu()
        self.assertIn("1. Ask a question", menu)
        self.assertIn("2. Add a device", menu)

if __name__ == "__main__":
    unittest.main()
