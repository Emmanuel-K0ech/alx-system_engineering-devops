#!/usr/bin/python3
"""subs module Documentation - Reddit API(No of Subscribers)"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit
    Args:
    subreddit(str): The name of the subreddit

    Return:
    int: The number of subscribers if exists otherwise return 0
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': '0x16-api_advanced'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Ensure the request was successful
        if response.status_code == 200:
            data = response.json().get("data", {})
            # Return the number of subscribers or 0 if not found
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
