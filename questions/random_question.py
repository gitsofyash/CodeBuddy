import random

from questions.leetcode_api import fetch_problemset_questions, format_problem

def fetch_random_leetcode_question():
    try:
        questions = fetch_problemset_questions()
        question = random.choice(questions)
        return format_problem(question)
    except Exception:
        return "Failed to fetch LeetCode questions."
