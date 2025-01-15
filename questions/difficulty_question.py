import random
import requests

def fetch_leetcode_question(difficulty="easy"):
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    if response.status_code == 200:
        questions = response.json()["stat_status_pairs"]
        difficulty_map = {"easy": 1, "medium": 2, "hard": 3}
        filtered = [q for q in questions if q["difficulty"]["level"] == difficulty_map.get(difficulty.lower(), 1)]
        question = random.choice(filtered)
        title = question["stat"]["question__title"]
        link = f"https://leetcode.com/problems/{question['stat']['question__title_slug']}/"
        total_acs = question["stat"]["total_acs"]
        total_submitted = question["stat"]["total_submitted"]
        acceptance_rate = (total_acs / total_submitted * 100) if total_submitted > 0 else 0
        
        return {
            'title': title,
            'difficulty': difficulty.capitalize(),
            'link': link,
            'acceptance_rate': acceptance_rate
        }
    else:
        return "Failed to fetch LeetCode questions."
