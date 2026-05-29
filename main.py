import argparse

from utils.data_storage import load_questions_completed, save_questions_completed

QUESTION_TYPES = ("random", "difficulty", "daily")
QUESTION_CHOICES = ("all", *QUESTION_TYPES)


def get_progressive_difficulty(questions_completed):
    if questions_completed >= 70:
        return "hard"
    if questions_completed >= 15:
        return "medium"
    return "easy"


def main(question_types=QUESTION_TYPES):
    for question_type in question_types:
        label = question_type.replace("_", " ").title()
        print(f"Sending {label} Question...")
        send_question(question_type)


def send_question(question_type="random"):
    """
    Fetches the question (random, difficulty-based, or daily) and sends it.
    Gradually increases difficulty based on the number of questions answered only for difficulty-based questions.
    """
    from questions.random_question import fetch_random_leetcode_question
    from questions.difficulty_question import fetch_leetcode_question
    from questions.daily_question import fetch_daily_leetcode
    from utils.send_message import send_message

    if question_type not in QUESTION_TYPES:
        raise ValueError(f"Unsupported question type: {question_type}")

    questions_completed = load_questions_completed()
    difficulty = get_progressive_difficulty(questions_completed)
    
    if question_type == "random":
        question = fetch_random_leetcode_question()
    elif question_type == "daily":
        question = fetch_daily_leetcode()
    else:
        question = fetch_leetcode_question(difficulty=difficulty)
    
    if isinstance(question, dict):
        message = (
            f"LeetCode {question['difficulty']} Question: {question['title']}\n"
            f"Link: {question['link']}\n"
            f"Acceptance Rate: {question['acceptance_rate']:.2f}%\n"
            f"Solutions: {question['solution_link']}\n"
            f"Discussion: {question['discussion_link']}\n"
            "Study flow: try it first, read hints, compare solutions, then write notes in your own words."
        )
        send_message(message)
        
        if question_type == "difficulty":
            save_questions_completed(questions_completed + 1)
    else:
        send_message(question or "Failed to fetch a LeetCode question.")

def parse_args():
    parser = argparse.ArgumentParser(description="Send free LeetCode practice push notifications.")
    parser.add_argument(
        "--type",
        choices=QUESTION_CHOICES,
        default="all",
        help="Question type to send. Defaults to all.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    selected_types = QUESTION_TYPES if args.type == "all" else (args.type,)
    main(selected_types)
