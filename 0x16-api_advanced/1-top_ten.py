#!/usr/bin/python3
"""Subscribers of a subreddit in Reddit"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
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
