import json
import os

QUESTIONS_FILE = "questions_completed.json"


def load_questions_completed():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("questions_completed", 0)
    return 0


def save_questions_completed(count):
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump({"questions_completed": count}, file, indent=2)
