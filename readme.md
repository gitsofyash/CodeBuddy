CodeBuddy - Daily Coding Challenge Notifications
Project Overview
CodeBuddy sends daily coding challenges from LeetCode to your WhatsApp. The bot fetches a daily LeetCode question based on difficulty progression and sends it to the user's WhatsApp. The app is automated to run daily at a specific time without any manual intervention.

Features
Fetch daily LeetCode questions based on difficulty.
Send questions to WhatsApp using Twilio API.
Ability to automatically run the script daily without keeping the system open.
Project Structure
bash
Copy code
CodeBuddy/
│
├── questions/             # Folder for storing questions (if applicable)
├── utils/                 # Folder for utility functions or scripts
├── venv/                  # Virtual environment folder
├── .env                   # Environment variables file
├── .gitignore             # Git ignore file
├── main.py                # Main application script
├── requirements.txt       # Dependencies for the project
└── script.bat             # Batch script to run the application (for local scheduling)
Requirements
Before running the project, ensure you have the following:

Python 3.x installed on your system.
Twilio account for WhatsApp API.
Git (optional if you're working with version control).
Windows OS for using the batch script (script.bat) to schedule tasks.
Installing Dependencies
Clone the repository to your local machine.
Navigate to the project folder in the terminal.
Install the required dependencies from the requirements.txt file:
bash
Copy code
pip install -r requirements.txt
Setting Up Twilio for WhatsApp
To send messages to your WhatsApp using Twilio, follow these steps:

Create a Twilio Account:

Visit Twilio and create an account.
After account creation, log in to the Twilio Console.
Set Up WhatsApp API:

In your Twilio Console, search for "WhatsApp" in the messaging section.
Get access to the WhatsApp Sandbox by following the steps in the WhatsApp Sandbox setup guide.
Get Your Twilio Credentials:

After setting up the sandbox, note down the following:
Account SID: Found in your Twilio Console.
Auth Token: Found in your Twilio Console.
WhatsApp Sandbox Number: whatsapp:+14155238886 or your own if you upgrade your account.
Your WhatsApp Number: The number to which the messages will be sent.
Create .env File:

In the root of your project directory, create a .env file and add your Twilio credentials like this:
env
Copy code
ACCOUNT_SID=your_account_sid
AUTH_TOKEN=your_auth_token
WHATSAPP_NUMBER=whatsapp:+14155238886  # Your Twilio WhatsApp number
YOUR_NUMBER=whatsapp:+1234567890     # Your personal WhatsApp number
Replace the placeholders with your actual Twilio account details and your personal WhatsApp number.

Running the Application
Running Locally
To run the script manually, use the following command:

bash
Copy code
python main.py
This will execute the script and send the LeetCode question to your WhatsApp.

Automating the Script Using Task Scheduler (Windows)
Open Task Scheduler by searching for it in the Start menu.
Click on Create Basic Task.
Follow the wizard:
Name: CodeBuddy Daily Task.
Trigger: Choose "Daily" and set the time (e.g., 5:00 PM).
Action: Choose "Start a Program" and browse for the script.bat file in the project folder.
Finish and ensure the task is running at the scheduled time daily.
script.bat (Batch Script)
The script.bat file is used to run the Python script automatically on Windows at a specific time (as set in Task Scheduler).

Contents of script.bat:

bat
Copy code
@echo off
cd /d "C:\path\to\your\project"
python main.py
Make sure to replace "C:\path\to\your\project" with the actual path to your project directory.

Conclusion
Now, you will receive daily LeetCode questions on WhatsApp without having to open the application. The app will fetch the question, increase the difficulty over time, and send it to you at the specified time daily.

This README.md should help you set up and run your project. Let me know if you need further clarification or additional details!