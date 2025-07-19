#!/usr/bin/python3
"""
Module that queries Reddit API to get subreddit subscriber count.

This module contains a function to retrieve the number of subscribers
for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query Reddit API and return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/temp_user)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except (requests.RequestException, KeyError, ValueError):
        return 0
