#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    if not subreddit:
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; reddit-api-client/1.0)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
    except Exception:
        pass
