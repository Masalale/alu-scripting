#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the titles of all hot articles, and prints a sorted count of
given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): The 'after' token for pagination.
                               Defaults to None.
        counts (dict, optional): A dictionary to store keyword counts.
                                 Defaults to None.
    """
    if counts is None:
        # Initialize counts dictionary from word_list, handling case-insensitivity
        # and duplicates by summing them up.
        counts = {}
        for word in word_list:
            lower_word = word.lower()
            counts[lower_word] = counts.get(lower_word, 0) + 1

        # For the final print, we need the counts of individual keywords,
        # so we reset the values to 0 after getting the unique keywords.
        # The initial aggregation was just to handle duplicates in word_list.
        # A better way is to just get unique words.
        final_counts = {word: 0 for word in counts.keys()}
        return count_words(subreddit, word_list, after, final_counts)

    # API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'python:alu-scripting:v1.0 (by /u/Masalale)'}
    params = {'after': after, 'limit': 100}

    try:
        # Make the API request, preventing redirects for invalid subreddits
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return  # Invalid subreddit or error, print nothing

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        # Process titles
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in title.split():
                if word in counts:
                    counts[word] += 1

        if after:
            # Recursive call for the next page
            count_words(subreddit, word_list, after, counts)
        else:
            # Base case: last page reached, print results
            # Filter out words with zero count
            filtered_counts = {k: v for k, v in counts.items() if v > 0}

            # Sort by count (desc) and then alphabetically (asc)
            sorted_items = sorted(
                filtered_counts.items(), key=lambda item: (-item[1], item[0])
            )

            for word, count in sorted_items:
                print(f"{word}: {count}")

    except requests.RequestException:
        return  # Network error, print nothing
