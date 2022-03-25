#!/usr/bin/python3
"""Module 0-gather_data_from_an_API GETS information from url and with id"""


import csv
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
    username = user['username']
    rows = []
    for task in todos:
        row = [uid, username, task['title'], str(task['completed'])]
        rows.append(row)
    filename = '{}.csv'.format(uid)
    with open(filename, 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for r in rows:
            writer.writerow(r)
