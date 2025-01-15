import random
import requests

def fetch_random_leetcode_question():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    if response.status_code == 200:
        questions = response.json()["stat_status_pairs"]
        question = random.choice(questions)
        title = question["stat"]["question__title"]
        link = f"https://leetcode.com/problems/{question['stat']['question__title_slug']}/"
        total_acs = question["stat"]["total_acs"]
        total_submitted = question["stat"]["total_submitted"]
        acceptance_rate = (total_acs / total_submitted * 100) if total_submitted > 0 else 0
        
        return {
            'title': title,
            'difficulty': "Medium",  # Default difficulty as Medium for random question
            'link': link,
            'acceptance_rate': acceptance_rate
        }
    else:
        return "Failed to fetch LeetCode questions."
