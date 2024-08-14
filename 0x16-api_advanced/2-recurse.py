#!/usr/bin/python3
""" 2-recurse module: queries the Reddit API to get all hot titles"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to get all hot titles for a given subreddit.

    Args:
    subreddit (str): name of the subreddit.
    hot_list (list): A list to accumulate the titles.
    after (str): The after parameter for pagination.

    Returns:
    list: A list containing the titles of all hot articles for the subreddit.
    """
    if hot_list is None:
        hot_list = []
    headers = {'User-Agent': '0x16-api_advanced'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False, 
                                params=parameters, timeout=10)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            next_after = data.get('after')
            for post in children:
                title = post.get('data', {}).get('title')
                if title:
                    hot_list.append(title)
            if next_after:
                return recurse(subreddit, hot_list, next_after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
