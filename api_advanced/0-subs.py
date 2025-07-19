#!/usr/bin/python3
"""
Module to query Reddit API and get subscriber count for subreddits.
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
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Google Chrome Version 126.0.6478.127'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
