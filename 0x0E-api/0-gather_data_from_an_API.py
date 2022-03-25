#!/usr/bin/python3
"""Module 0-gather_data_from_an_API GETS information from url and with id"""


import json
import sys
from urllib import request


if __name__ == '__main__':
    turl = 'https://jsonplaceholder.typicode.com/todos'
    uurl = 'https://jsonplaceholder.typicode.com/users'
    uid = sys.argv[1]
    with request.urlopen("{}/{}".format(uurl, uid)) as response:
        user = json.loads(response.read().decode('utf8'))
    with request.urlopen("{}/?userId={}".format(turl, uid)) as response:
        todos = json.loads(response.read().decode('utf8'))
    employee_name = user['name']
    num_done = 0
    tasks_done = []
    tot_tasks = 0
    for task in todos:
        if task['completed']:
            num_done += 1
            tasks_done.append(task['title'])
        tot_tasks += 1
    print("Employee {} is done with tasks".format(employee_name), end="")
    print("({}/{}):".format(num_done, tot_tasks))
    for title in tasks_done:
        print("\t {}".format(title))
