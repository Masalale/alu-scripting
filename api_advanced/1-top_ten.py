#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    if not subreddit or not isinstance(subreddit, str):
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/pythonbot)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    except Exception:
        return
