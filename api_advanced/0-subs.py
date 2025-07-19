#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and return the
number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API and return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit.
             Returns 0 if the subreddit is invalid or if there's an error.

    Note:
        This function does not follow redirects, as invalid subreddits may
        redirect to search results.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'python:alu-scripting:v1.0 (by /u/Masalale)'}

    try:
        # Don't follow redirects - invalid subreddits may redirect to search
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
