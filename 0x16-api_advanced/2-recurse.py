#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/binyammamo)"
}
def recurse(subreddit, hot_list=[], after=None, count = 0):
    if after is None:
        return hot_list
    url = f"https://www.reddit.com/r/{subreddit}.json?limit=1&after={after}"
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if (resp.json() is None):
        return None
    title = resp.json()["data"]["children"][0]["data"]["title"]
    after = resp.json()["data"]["after"]
    # print(after, "=>", resp.json()["data"]["children"][0]["data"]["title"])
    count += 1
    hot_list.append(title)
    # print('.')
    recurse(subreddit, hot_list, after, count)
    # print(hot_list)
    return hot_list
