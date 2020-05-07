#!/usr/bin/python3
"""Pagination using recursion"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': '1.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)

    if response.status_code == 200:
        r = response.json()
        x = r.get('data').get('children')
        aft_val = r.get('data').get('after')
        a = list(map(lambda i: hot_list.append(i.get('data').get('title')), x))
        if not aft_val:
            return (hot_list)
        return (recurse(subreddit, hot_list, aft_val))
    else:
        return(None)
