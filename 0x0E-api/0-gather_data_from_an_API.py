#!/usr/bin/python3
"""Module 0-gather_data_from_an_API GETS information from url and with id"""


from urllib import request
import sys
import json


if __name__ == '__main__':
    turl = 'https://jsonplaceholder.typicode.com/todos'
    uurl = 'https://jsonplaceholder.typicode.com/users'
    uid = sys.argv[1]
    with request.urlopen("{}/{}".format(uurl, uid)) as response:
        user = json.loads(response.read().decode('utf8'))
    with request.urlopen(turl) as response:
        todos = json.loads(response.read().decode('utf8'))
    employee_name = user['name']
    num_done = 0
    tasks_done = []
    start_pos = 0 + ((int(uid) - 1) * 20)
    for task in todos[start_pos:start_pos+20]:
        if task['completed']:
            num_done += 1
            tasks_done.append(task['title'])
    print("Employee {} is done with tasks".format(employee_name), end="")
    print("({}/20):".format(num_done))
    for title in tasks_done:
        print("\t {}".format(title))
