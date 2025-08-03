#!/usr/bin/python3
"""Define top_ten function"""
import requests

def top_ten(subreddit):
    """
        Query the Reddit API and prints the titles of the first 10 hot posts
        listed for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:api_advanced:v1.0.0 (by /u/Masalale)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            if not children:
                print(None)
                return
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
