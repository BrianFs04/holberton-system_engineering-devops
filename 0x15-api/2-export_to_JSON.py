#!/usr/bin/python3
"""Exporting to JSON"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1]))
    task = requests.get(url + 'todos?userId={}'.format(sys.argv[1]))

    user_list = user.json()
    task_list = task.json()

    arc_name = '{}.json'.format(user_list.get('id'))

    with open(arc_name, mode='w') as f:
        data = {}
        data[user_list.get('id')] = []

        for task in task_list:
            data[user_list.get('id')].append({
                'task': task.get('title'),
                "completed": task.get('completed'),
                "username": user_list.get('username')
            })

        json.dump(data, f)
