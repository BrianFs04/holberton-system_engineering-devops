#!/usr/bin/python3
"""Exporting to CSV"""
import csv
import sys
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1]))
    task = requests.get(url + 'todos?userId={}'.format(sys.argv[1]))

    user_list = user.json()
    task_list = task.json()
    completed_tasks = 0
    all_tasks = 0

    for task in task_list:
        completed = task.get('completed')
        if completed:
            completed_tasks += 1
        all_tasks += 1

    print('Employee {} is done with tasks ({}/{}):'
          .format(user_list.get('name'), completed_tasks, all_tasks))

    for task in task_list:
        completed = task.get('completed')
        task_title = task.get('title')
        if completed:
            print('\t {}'.format(task_title))

    arc_name = '{}.csv'.format(user_list.get('id'))
    with open(arc_name, mode='w') as two:
        writer = csv.writer(two, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in task_list:
            writer.writerow([user_list.get('id'), user_list.get('username'),
                             task.get('completed'), task.get('title')])
