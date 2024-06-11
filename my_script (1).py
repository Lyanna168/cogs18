"""Script to run some part of my project."""
from my_module.classes import Chatbot, KnowledgeBase, User
from scripts.allocation.py import allocate_resources
from scripts.comment.py import add_comment

def main():
    knowledge_base = KnowledgeBase()
    chatbot = Chatbot(knowledge_base)

    user = User("Alice")
    user.add_device("washing machine", "LG1234", 2018)

    question = "My washing machine is not spinning, what should I do?"
    response = user.ask_question(chatbot, question)
    print(f"Chatbot: {response}")

    allocation_status = allocate_resources(user, "washing machine")
    print(allocation_status)

    comment_status = add_comment(user, "Thank you for the help!")
    print(comment_status)

if __name__ == "__main__":
    main()
