#!/usr/bin/python3
"""1-top_ten module Documentation - Title of top 10 reddits"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    Args:
    subreddit(str): The name of the subreddit

    Return: None if subreddit is not valid
    """
    if not isinstance(subreddit, str) or not subreddit:
        print("Invalid subreddit name.")
        return
    headers = {'User-Agent': '0x16-api_advanced'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                params=parameters, timeout=10)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children:
                print("No posts found.")
                return
            for post in children:
                title = post.get('data', {}).get('title', 'No title')
                print(title)
        else:
            print(None)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
