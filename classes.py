"""
Classes used throughout the project.
"""

from my_module.enhancers import enhance_query_with_device_info

class KnowledgeBase:
    def __init__(self):
        self.static_knowledge = {
            "my washing machine is not spinning, what should i do? model: lg1234, year: 2018": "Please check if the power is properly connected, or if the door is not closed tightly.",
            "refrigerator not cooling": "Please check if the thermostat is set correctly, or if the vents are blocked.",
            "light bulb not working": "Please check if the bulb is burnt out, or if the switch is working properly."
        }

    def search_knowledge(self, query):
        query = query.lower()  # 确保查询是小写形式
        print(f"DEBUG: searching for query = {query}")
        for key in self.static_knowledge:
            if key in query:
                return self.static_knowledge[key]
        return "Sorry, I couldn't find any relevant information. Please provide more details."

class Chatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def get_response(self, user, user_input):
        device_details = user.get_device_details()
        enhanced_query = enhance_query_with_device_info(user_input, device_details)
        response = self.knowledge_base.search_knowledge(enhanced_query)
        return response

class User:
    def __init__(self, name):
        self.name = name
        self.device_info = {}

    def add_device(self, device_name, model, year):
        self.device_info[device_name] = {"model": model, "year": year}

    def get_device_details(self):
        return next(iter(self.device_info.values()))

    def ask_question(self, chatbot, question):
        return chatbot.get_response(self, question)




