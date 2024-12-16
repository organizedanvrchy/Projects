import requests

def fetch_questions(category, amount=10):
    """Fetch questions from OpenTDB based on category and shuffle them."""
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&type=boolean"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0:  # Success
            return data["results"]
        else:
            print("No questions found. Please try different settings.")
            return []
    else:
        print("Failed to fetch questions from the API. Please check your connection.")
        return []
