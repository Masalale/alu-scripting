#!/usr/bin/python3
"""
This module provides a function to query the Reddit API for the number of
subscribers of a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
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
