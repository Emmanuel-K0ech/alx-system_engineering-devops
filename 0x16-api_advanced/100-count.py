#!/usr/bin/python3
"""100-count Module: Recursive function that queries
the Reddit API to count keywords"""
import requests
import re


def count_words(subreddit, word_list, after=None, count_dic=None):
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
    if count_dic is None:
        count_dic = {word.lower(): 0 for word in word_list}
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
                title = post.get('data', {}).get('title', '')
                title_lower = title.lower()
                for word in count_dic:
                    count_dic[word] += len(re.findall(r'\b{}\b'.format(
                        re.escape(word)), title_lower))
            if next_after:
                return count_words(subreddit, word_list, after=next_after,
                                   count_dic=count_dic)
            else:
                # Sort the dictionary by count and print results
                sorted_counts = sorted(count_dic.items(), key=lambda x: x[1],
                                       reverse=True)
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            print("Invalid subreddit or request failed.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
