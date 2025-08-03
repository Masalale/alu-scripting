#!/usr/bin/python3
"""Define top_ten function"""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            results = response.json().get("data")
            if results:
                children = results.get("children")
                if children:
                    for child in children:
                        print(child.get("data").get("title"))
                    return
    except requests.exceptions.RequestException:
        pass
    print("None")
