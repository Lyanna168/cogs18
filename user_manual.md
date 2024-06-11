# Repair Assistant Chatbot User Manual

## Introduction
This user manual explains how to use the Repair Assistant Chatbot to get help with home appliance and furniture repairs. The chatbot is designed to assist single women living alone by providing step-by-step guidance on fixing common household issues.

## How to use
Running the Application
To run the Repair Assistant Chatbot application, follow these steps:

1.Set Up Your Environment:
Ensure you have Python installed on your system. 
You can download it from python.org.
Install the required dependencies by running the following command in your terminal:
pip install -r requirements.txt

2.Navigate to the Project Directory:
Open your terminal or command prompt.
Navigate to the project directory where the Repair Assistant Chatbot is located. For example:
cd /path/to/your/Project_COGS18_SP24
Run the Main Script:

3.Execute the main script to start the chatbot application:
python scripts/main.py
Interacting with the Chatbot:

4.Once the chatbot is running, you will be prompted to enter your name.
Add details about your home appliances using the provided commands. 


5.Ask the chatbot questions about your appliances. For example:
My washing machine is not spinning, what should I do?
Features and Commands

6.Adding a Device
To add a device, use the add_device command followed by the device name, model, and year of manufacture. Example:
add_device washing_machine LG1234 2018

7.Asking a Question
To ask the chatbot a question, simply type your question after adding the relevant device. The chatbot will use the device information to provide a more accurate response. 
Example:
My washing machine is not spinning, what should I do?


## Example Interactions
Adding a Device:
add_device washing_machine LG1234 2018

Output:
Device added: washing machine, Model: LG1234, Year: 2018

Asking a Question:
My washing machine is not spinning, what should I do?

Output:
Please check if the power is properly connected, or if the door is not closed tightly.

## Troubleshooting
If you encounter any issues, consider the following steps:

Check Dependencies: Ensure all required dependencies are installed by checking the requirements.txt file.

Review Documentation: Refer to the docs directory for detailed project documentation.

Debugging: Use print statements or a debugger to trace and fix any issues in the code.

Contact Information
For further assistance, contact the project team at support@example.com.

By following this user manual, you should be able to effectively use the Repair Assistant Chatbot to get help with your home appliance and furniture repairs. Enjoy the peace of mind that comes with knowing you have a reliable assistant to guide you through any household repair challenges!
