#!/usr/bin/python3
"""Module 0-gather_data_from_an_API GETS information from url and with id"""


import json
import sys
from urllib import request


if __name__ == '__main__':
    turl = 'https://jsonplaceholder.typicode.com/todos'
    uurl = 'https://jsonplaceholder.typicode.com/users'
    uid = str(sys.argv[1])
    with request.urlopen("{}/{}".format(uurl, uid)) as response:
        user = json.loads(response.read().decode('utf8'))
    with request.urlopen("{}/?userId={}".format(turl, uid)) as response:
        todos = json.loads(response.read().decode('utf8'))
    name = user['name']
    username = user['username']
    data, tasks, tasks_done = {}, [], []
    tot_tasks, num_done = len(todos), 0
    for task in todos:
        if task['completed']:
            num_done += 1
            tasks_done.append(task['title'])
        row = {
            "task": task['title'],
            "completed": str(task['completed']).lower(),
            "username": username
            }
        tasks.append(row)
    data[uid] = tasks
    print("Employee {} is done with tasks".format(name), end="")
    print("({}/{}):".format(num_done, tot_tasks))
    for title in tasks_done:
        print("\t {}".format(title))
    filename = '{}.json'.format(uid)
    with open(filename, 'w+', encoding='UTF8') as f:
        json.dump(data, f)
