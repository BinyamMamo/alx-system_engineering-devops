#!/usr/bin/python3
"""
0-main
"""

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        number_of_subscribers(sys.argv[1])
