"""
Manage user interaction menus.
"""

def display_menu():
    """
    Display the main menu for user interaction.
    
    Returns:
    str: Menu options.
    """
    menu = """
    1. Ask a question
    2. Add a device
    3. Allocate resources
    4. Add a comment
    5. Simulate device action
    6. Exit
    """
    return menu

def get_user_choice():
    """
    Get the user's menu choice.
    
    Returns:
    str: The user's menu choice.
    """
    return input("Choose an option: ")

