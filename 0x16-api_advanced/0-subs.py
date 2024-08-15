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
        'User-Agent': 'linux:myapp:v1.0.0 (by /u/Helpful_Bread_7117)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
