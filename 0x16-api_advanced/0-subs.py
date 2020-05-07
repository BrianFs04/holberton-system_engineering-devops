#!/usr/bin/python3
"""Subscribers of a subreddit in Reddit"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': '1.0'
    }
    response = requests.get(url, allow_redirects=False, headers=headers)
    r = response.json()
    if response:
        num_subs = r.get('data').get('subscribers')
        return (num_subs)
    else:
        return (0)
