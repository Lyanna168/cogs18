from my_module.classes import Chatbot, KnowledgeBase, User
from scripts.allocation import allocate_resources
from scripts.comment import add_comment
from scripts.npc_action import simulate_device_action
from scripts.player_menu import display_menu, get_user_choice
from scripts.stat_check import check_device_status

def main():
    knowledge_base = KnowledgeBase()
    chatbot = Chatbot(knowledge_base)

    user = User("Alice")
    user.add_device("washing machine", "LG1234", 2018)

    while True:
        print(display_menu())
        choice = get_user_choice()

        if choice == "1":
            question = input("Enter your question: ")
            response = user.ask_question(chatbot, question)
            print(f"Chatbot: {response}")

        elif choice == "2":
            device_name = input("Enter device name: ")
            model = input("Enter device model: ")
            year = int(input("Enter device year: "))
            user.add_device(device_name, model, year)
            print(f"Device {device_name} added.")

        elif choice == "3":
            device_name = input("Enter device name to allocate resources for: ")
            allocation_status = allocate_resources(user, device_name)
            print(allocation_status)

        elif choice == "4":
            comment = input("Enter your comment: ")
            comment_status = add_comment(user, comment)
            print(comment_status)

        elif choice == "5":
            device_name = input("Enter device name: ")
            action = input("Enter action to simulate: ")
            simulation_result = simulate_device_action(device_name, action)
            print(simulation_result)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

