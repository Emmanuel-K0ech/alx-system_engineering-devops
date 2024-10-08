#!/usr/bin/python3
"""Function: Query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0\
        (by /u/Helpful_Bread_7117)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
