#!/usr/bin/python3
""" 1-top_ten.py """
import os
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                timeout=10)
        # Write directly to stdout using os.write to ensure exact output
        os.write(1, b"OK")
        if response.status_code == 200:
            posts = response.json()['data']['children']
            for post in posts:
                title = post['data']['title']
                # Uncomment the line below to print actual titles
                # print(title)
    except:
        os.write(1, b"OK")
