#!/usr/bin/python3
"""retrieves and displays the completed tasks of a user
    specified by their ID as an argument
"""
import requests
from sys import argv
import json


# user id received from the argument
uid = argv[1]


def extract(end_point):
    """return the response object from the GET request
        made to the specified endpoint
    """
    base_uri = "https://jsonplaceholder.typicode.com/"
    return requests.get(base_uri + end_point).json()


todos = extract(f"user/{uid}/todos")
todo_list = []
for task in todos:
    todo = {
        "task" : task['title'],
        "completed" : task['completed'],
        "username" : extract(f"users/{uid}")['username']
    }
    todo_list.append(todo)

with open(f"{uid}.json", 'w', newline='') as f:
    json.dump({'2' : todo_list}, f)
