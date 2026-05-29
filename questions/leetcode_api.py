import requests

LEETCODE_PROBLEMSET_URL = "https://leetcode.com/api/problems/all/"
REQUEST_TIMEOUT_SECONDS = 15

DIFFICULTY_LEVELS = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

DIFFICULTY_NAMES = {
    1: "Easy",
    2: "Medium",
    3: "Hard",
}


def fetch_problemset_questions():
    response = requests.get(LEETCODE_PROBLEMSET_URL, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()["stat_status_pairs"]


def format_problem(question):
    stat = question["stat"]
    slug = stat["question__title_slug"]
    total_submitted = stat["total_submitted"]
    acceptance_rate = (stat["total_acs"] / total_submitted * 100) if total_submitted else 0

    return {
        "title": stat["question__title"],
        "difficulty": DIFFICULTY_NAMES.get(question["difficulty"]["level"], "Unknown"),
        "link": f"https://leetcode.com/problems/{slug}/",
        "solution_link": f"https://leetcode.com/problems/{slug}/solutions/",
        "discussion_link": f"https://leetcode.com/problems/{slug}/discuss/",
        "acceptance_rate": acceptance_rate,
    }
