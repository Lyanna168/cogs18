import unittest
import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from scripts.npc_action import simulate_device_action

class TestNpcAction(unittest.TestCase):
    def test_simulate_device_action(self):
        result = simulate_device_action("washing machine", "start cycle")
        self.assertEqual(result, "Simulating start cycle on washing machine.")

if __name__ == "__main__":
    unittest.main()


