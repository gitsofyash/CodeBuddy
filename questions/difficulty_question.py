import random

from questions.leetcode_api import DIFFICULTY_LEVELS, fetch_problemset_questions, format_problem

def fetch_leetcode_question(difficulty="easy"):
    try:
        questions = fetch_problemset_questions()
        difficulty_level = DIFFICULTY_LEVELS.get(difficulty.lower(), DIFFICULTY_LEVELS["easy"])
        filtered = [q for q in questions if q["difficulty"]["level"] == difficulty_level]
        if not filtered:
            return f"No {difficulty} LeetCode questions found."

        question = random.choice(filtered)
        return format_problem(question)
    except Exception:
        return "Failed to fetch LeetCode questions."
