import unittest
import sys
import os

# 获取项目目录的绝对路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from my_module.functions import log_interaction, format_response, validate_user_input, retrieve_device_info
from my_module.enhancers import enhance_query_with_device_info
from my_module.classes import User, Chatbot, KnowledgeBase

class TestFunctions(unittest.TestCase):
    def test_log_interaction(self):
        knowledge_base = KnowledgeBase()
        chatbot = Chatbot(knowledge_base)
        user = User("Alice")
        user.add_device("washing machine", "LG1234", 2018)
        question = "My washing machine is not spinning, what should I do?"
        response = chatbot.get_response(user, question)
        
        # 捕获日志输出
        with self.assertLogs(level='INFO') as log:
            log_interaction(user, question, response)
            self.assertIn("User: Alice | Question: My washing machine is not spinning, what should I do? | Response: Please check if the power is properly connected, or if the door is not closed tightly.", log.output[0])

    def test_format_response(self):
        response = "this is a test response"
        formatted_response = format_response(response)
        self.assertEqual(formatted_response, "This is a test response.")

        response = "This is another test response."
        formatted_response = format_response(response)
        self.assertEqual(formatted_response, "This is another test response.")

    def test_validate_user_input(self):
        valid_input = "What is the problem?"
        invalid_input = "   "
        self.assertTrue(validate_user_input(valid_input))
        self.assertFalse(validate_user_input(invalid_input))

    def test_enhance_query_with_device_info(self):
        query = "My washing machine is not spinning"
        device_info = {"model": "LG1234", "year": 2018}
        enhanced_query = enhance_query_with_device_info(query, device_info)
        expected_query = "my washing machine is not spinning model: lg1234, year: 2018"
        self.assertEqual(enhanced_query, expected_query)

    def test_retrieve_device_info(self):
        user = User("Alice")
        user.add_device("washing machine", "LG1234", 2018)
        device_info = retrieve_device_info(user, "washing machine")
        self.assertEqual(device_info, {"model": "LG1234", "year": 2018})
        
        # 测试不存在的设备
        no_device_info = retrieve_device_info(user, "refrigerator")
        self.assertIsNone(no_device_info)

    def test_user_interaction(self):
        knowledge_base = KnowledgeBase()
        chatbot = Chatbot(knowledge_base)
        user = User("Alice")
        user.add_device("washing machine", "LG1234", 2018)
        question = "My washing machine is not spinning, what should I do?"
        response = user.ask_question(chatbot, question)
        print(f"DEBUG: response = {response}")
        self.assertIn("Please check if the power is properly connected", response)

if __name__ == "__main__":
    unittest.main()


                 
    