import json
import requests

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"
REQUEST_TIMEOUT_SECONDS = 15


def fetch_daily_leetcode():
    """
    Fetches the daily LeetCode question using GraphQL.
    """
    query = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                title
                titleSlug
                hasVideoSolution
                hasSolution
                content
            }
        }
    }
    """
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.post(
            LEETCODE_GRAPHQL_URL,
            json={"query": query},
            headers=headers,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        
        data = response.json()
        question_data = data["data"]["activeDailyCodingChallengeQuestion"]
        slug = question_data["question"]["titleSlug"]

        return {
            "title": question_data["question"]["title"],
            "difficulty": question_data["question"]["difficulty"],
            "link": f"https://leetcode.com{question_data['link']}",
            "solution_link": f"https://leetcode.com/problems/{slug}/solutions/",
            "discussion_link": f"https://leetcode.com/problems/{slug}/discuss/",
            "acceptance_rate": question_data["question"]["acRate"],
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
