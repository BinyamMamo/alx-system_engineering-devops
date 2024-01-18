#!/usr/bin/python3
"""
retrieves the number of subscribers for a given subreddit
using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/binyammamo)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json()["data"]["subscribers"]
    return results
