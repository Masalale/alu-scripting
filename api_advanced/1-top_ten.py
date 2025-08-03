#!/usr/bin/python3
"""
This module provides a function to fetch and print the top 10 hot posts
from a given subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None. Prints the titles of the top 10 hot posts, one per line.
        If the subreddit is not valid or an error occurs, it prints "None".
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            results = response.json().get("data")
            if results:
                children = results.get("children")
                if children:
                    for child in children:
                        print(child.get("data").get("title"))
                    return
    except requests.exceptions.RequestException:
        pass
    print("None")
