#!/usr/bin/python3
""" 1-top_ten.py """

import requests


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        else:
            print("None")
    except (requests.RequestException, KeyError, ValueError):
        print("None")
