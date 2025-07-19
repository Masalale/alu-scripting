#!/usr/bin/python3
""" main function 1"""
import sys

if __name__ == "__main__":
    hot_ten = __import__('1-top_ten').top_ten
    if(len(sys.argv)<2):
        print("Please pass an argument for the subreddit to search.")
    else:
        hot_ten(sys.argv[1])
