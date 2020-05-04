#!/usr/bin/python3
"""Exporting to JSON a list of dictionaries"""
import json
import sys
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/')
    task = requests.get(url + 'todos/')

    user_list = user.json()
    task_list = task.json()

    with open('todo_all_employees.json', mode='w') as f:
        data = {}
        for user in user_list:
            data[user.get('id')] = []

            for task in task_list:
                data[user.get('id')].append({
                    'task': task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')
                })

        json.dump(data, f)
