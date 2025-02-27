import sys
import requests
import time

def get_user_location(api_url):
    """
    Fetches and prints the location of a GitHub user.

    Args:
        api_url (str): The full GitHub API URL of the user.

    Returns:
        None
    """
    try:
        response = requests.get(api_url)
        
        # Handle rate limit exceeded
        if response.status_code == 403:
            reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
            minutes_until_reset = max(0, (reset_time - time.time()) // 60)
            print(f"Reset in {int(minutes_until_reset)} min")
            return
        
        # Handle user not found
        if response.status_code == 404:
            print("Not found")
            return
        
        # Handle successful response
        if response.status_code == 200:
            user_data = response.json()
            location = user_data.get("location", "Not found")
            print(location)
            return
        
        # Handle other errors
        print("Error: Unable to fetch data")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
    else:
        get_user_location(sys.argv[1])
