import json
import requests


# Function to fetch the daily LeetCode question using GraphQL
def fetch_daily_leetcode(difficulty="medium"):
    """
    Fetches the daily LeetCode question using GraphQL, with the option to filter by difficulty.
    """
    url = "https://leetcode.com/graphql"
    
    # GraphQL query to get daily question details
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
    
    # Headers to mimic browser request
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        # Make the request
        response = requests.post(url, json={'query': query}, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse the response
        data = response.json()
        question_data = data['data']['activeDailyCodingChallengeQuestion']

        # Format the data
        daily_question = {
            'title': question_data['question']['title'],
            'difficulty': question_data['question']['difficulty'],
            'link': f"https://leetcode.com{question_data['link']}",
            'acceptance_rate': question_data['question']['acRate']
        }
        
        return daily_question
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
