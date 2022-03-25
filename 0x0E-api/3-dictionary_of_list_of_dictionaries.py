#!/usr/bin/python3
"""Module 0-gather_data_from_an_API GETS information from url and with id"""


import json
import requests
import sys
from urllib import request



if __name__ == '__main__':
    turl = 'https://jsonplaceholder.typicode.com/todos'
    uurl = 'https://jsonplaceholder.typicode.com/users'
    data = {}
    with request.urlopen("{}".format(uurl)) as response:
        users = json.loads(response.read().decode('utf8'))
    for user in users:
        uid = user['id']
        todos = requests.get("{}/?userId={}".format(turl, uid)).json()
        json_list = []
        for task in todos:
            json_task = {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            json_list.append(json_task)
        data[str(uid)] = json_list
    filename = "todo_all_employees.json"
    with open(filename, 'w+', encoding='UTF8') as f:
        json.dump(data, f)
