#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/binyammamo)"
    }

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        return 0
    result = resp.json()
    result = result["data"]["children"]
    i = 0
    while i < 10:
        print(i + 1, " ", result[i]["data"]["title"])
        i = i + 1