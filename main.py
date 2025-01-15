from questions.random_question import fetch_random_leetcode_question
from questions.difficulty_question import fetch_leetcode_question
from questions.daily_question import fetch_daily_leetcode
from utils.send_message import send_whatsapp_message
from utils.data_storage import load_questions_completed, save_questions_completed

def main():
    # Load the current number of questions completed
    questions_completed = load_questions_completed()

    # Determine the difficulty level based on the number of questions answered
    if questions_completed >= 70:
        difficulty = "hard"
    elif questions_completed >= 15:
        difficulty = "medium"
    else:
        difficulty = "easy"

    # Fetch and send the question
    print("Sending Random Question ...")
    send_question_to_whatsapp("random")

    print("Sending Difficulty-Based Question...")
    send_question_to_whatsapp("difficulty")

    print("Sending Daily Question...")
    send_question_to_whatsapp("daily")

def send_question_to_whatsapp(question_type="random"):
    """
    Fetches the question (random, difficulty-based, or daily) and sends it to WhatsApp.
    Gradually increases difficulty based on the number of questions answered only for difficulty-based questions.
    """
    # Load the current number of questions completed
    questions_completed = load_questions_completed()

    # Initialize difficulty based on the number of questions answered
    if question_type == "difficulty":
        if questions_completed >= 70:
            difficulty = "hard"
        elif questions_completed >= 15:
            difficulty = "medium"
        else:
            difficulty = "easy"
    else:
        difficulty = "easy"  # Default difficulty for other question types (random, daily)
    
    # Fetch question based on type
    if question_type == "random":
        question = fetch_random_leetcode_question()
    elif question_type == "daily":
        question = fetch_daily_leetcode(difficulty=difficulty)
    else:  # difficulty-based
        question = fetch_leetcode_question(difficulty=difficulty)
    
    if isinstance(question, dict):
        message = (
            f"LeetCode {question['difficulty']} Question: {question['title']}\n"
            f"Link: {question['link']}\n"
            f"Acceptance Rate: {question['acceptance_rate']}%"
        )
        send_whatsapp_message(message)
        
        # Increment and save the number of questions completed (only for difficulty-based)
        if question_type == "difficulty":
            save_questions_completed(questions_completed + 1)
    else:
        send_whatsapp_message(question)

if __name__ == "__main__":
    main()
