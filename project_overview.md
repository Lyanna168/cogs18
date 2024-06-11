## Repair Assistant Chatbot

The Repair Assistant Chatbot is a Python-based application designed to assist single women with home appliance and furniture repairs. The chatbot provides answers to common issues related to household devices, offering helpful suggestions based on a static knowledge base. The chatbot can enhance its responses by incorporating specific details about the user's devices, such as the model and production year, ensuring more accurate and relevant assistance.

## Key Features:

Query Handling:
Ask the chatbot questions about your appliances to receive helpful advice. The chatbot uses a static knowledge base to provide solutions to common problems.

Resource Allocation:
Based on the device issue, the chatbot can suggest resources or steps for repairs. This ensures you have all the necessary information to fix your appliance.

User Feedback:
You can provide feedback or comments about the chatbot's suggestions. This helps improve the system and ensures it remains effective.

Action Simulation:
The chatbot can simulate actions on devices to demonstrate possible solutions. This visual aid can help you better understand the repair process.

## Example Interactions
Adding a Device:
add_device washing_machine LG1234 2018

Output:
Device added: washing machine, Model: LG1234, Year: 2018

Asking a Question:
My washing machine is not spinning, what should I do?

Output:
Please check if the power is properly connected, or if the door is not closed tightly.

##  Modules and Scripts:

Modules:

my_module/classes.py: Defines core classes like Chatbot, KnowledgeBase, and User.
my_module/functions.py: Contains helper functions for logging, input validation, response formatting, and query enhancement.
my_module/test_functions.py: Contains test cases for the functions and classes to ensure they work correctly.
Scripts:

scripts/allocation.py: Handles resource allocation for device repairs.
scripts/comment.py: Manages user comments or feedback.
scripts/main.py: Main script to run the chatbot application.
scripts/npc_action.py: Simulates actions on devices.
scripts/player_menu.py: Manages user interaction menus.
scripts/stat_check.py: Checks the status of various components.
Data:

data/device_data.json: Contains sample data for different devices, including their names, models, years, and common issues.
Documentation:

docs/project_overview.md: Provides an overview of the project, its purpose, and its structure.
docs/user_manual.md: Explains how to use the application, including running the main script and using the menu options.
docs/api_documentation.md: Provides documentation for the API endpoints or internal functions.
Tests:

tests/test_allocation.py: Tests the allocation functions.
tests/test_comment.py: Tests the comment functions.
tests/test_functions.py: Tests the functions from my_module/functions.py.
tests/test_npc_action.py: Tests the NPC action functions.
tests/test_player_menu.py: Tests the player menu functions.
tests/test_stat_check.py: Tests the status check functions.

## Troubleshooting
If you encounter any issues, consider the following steps:

Check Dependencies: Ensure all required dependencies are installed by checking the requirements.txt file.

Review Documentation: Refer to the docs directory for detailed project documentation.

Debugging: Use print statements or a debugger to trace and fix any issues in the code.

## Contact Information
For further assistance, contact the project team at support@example.com.

By following this user manual, you should be able to effectively use the Repair Assistant Chatbot to get help with your home appliance and furniture repairs. Enjoy the peace of mind that comes with knowing you have a reliable assistant to guide you through any household repair challenges!
