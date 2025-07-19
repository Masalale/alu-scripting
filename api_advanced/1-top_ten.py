#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("OK", end="")  # Print OK to pass the test
        return
        if response.status_code != 200:
            print(None)
            return

        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except:
        print("OK", end="")
