#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    # API endpoint for hot posts, limit to 10 posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'python:alu-scripting:v1.0 (by /u/Masalale)'}

    try:
        # Don't follow redirects - invalid subreddits may redirect to search
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
