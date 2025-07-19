#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): A token used for pagination to get the next page of results.

    Returns:
        list: A list of titles of all hot articles.
              Returns None if the subreddit is invalid or an error occurs.
    """
    # Construct the URL for the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'python:alu-scripting:v1.0 (by /u/Masalale)'}
    # Parameters for the request, including pagination token
    params = {'after': after}

    try:
        # Make the API request, preventing redirects for invalid subreddits
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        # If the subreddit is invalid or an error occurs, return None
        if response.status_code != 200:
            return None

        # Parse the JSON response
        data = response.json()
        # Extract the list of posts and the 'after' token for the next page
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')

        # Add the titles of the posts to the hot_list
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        # If there is a next page, make a recursive call
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            # If there are no more pages, return the list of titles
            return hot_list

    except requests.RequestException:
        # Return None if a request-related error occurs
        return None
