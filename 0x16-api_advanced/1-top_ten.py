#!/usr/bin/python3
"""Titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': '1.0'
    }
    response = requests.get(url, allow_redirects=False, headers=headers)
    r = response.json()

    if response:
        first = r.get('data').get('children')
        for i in first[:10]:
            print(i.get('data').get('title'))
    else:
        print(None)
