#!/usr/bin/python3
"""100-count Module: Recursive function that queries
the Reddit API to count keywords"""
import requests


def count_words(subreddit, word_list, instance={}, after="", count=0):
    """
    Parses the titles of all hot articles for a given subreddit and counts
    of the given keywords.

    Args:
    subreddit (str): The name of the subreddit.
    word_list (list): A list of keywords to count in titles.
    after (str, optional): The after parameter for pagination.
    count_dic (dict, optional): A dictionary to accumulate the keyword counts.

    Returns: None
    """
    if instance is None:
        instance = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0\
            (by /u/Helpful_Bread_7117)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
    except requests.exceptions.RequestException:
        print("")
        return
    except ValueError:
        print("")
        return
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())
                if word not in instance:
                    instance[word] = times
                else:
                    instance[word] += times
    if after is None:
        if not instance:
            print("")
            return
        instance = sorted(instance.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instance:
            print(f"{k}: {v}")
    else:
        count_words(subreddit, word_list, instance, after, count)
