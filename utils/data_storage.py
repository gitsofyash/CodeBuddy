import json
import os

QUESTIONS_FILE = 'questions_completed.json'

# Function to load the number of questions completed
def load_questions_completed():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r') as file:
            data = json.load(file)
            return data.get('questions_completed', 0)
    return 0

# Function to save the number of questions completed
def save_questions_completed(count):
    with open(QUESTIONS_FILE, 'w') as file:
        json.dump({'questions_completed': count}, file)
