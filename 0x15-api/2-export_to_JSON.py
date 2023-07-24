#!/usr/bin/python3
"""
Extracts a user's todos from a JSON API and saves them in a JSON file.
"""

import json
import requests
from sys import argv


def extract(end_point):
    """return the response object from the GET request
        made to the specified endpoint
    """
    base_uri = "https://jsonplaceholder.typicode.com/"
    return requests.get(base_uri + end_point).json()


if __name__ == "main":
    # user id received from the argument
    uid = argv[1]

    todos = extract(f"user/{uid}/todos")
    todo_list = []
    for task in todos:
        todo = {
            "task": task['title'],
            "completed": task['completed'],
            "username": extract(f"users/{uid}")['username']
        }
        todo_list.append(todo)

    with open(f"{uid}.json", 'w', newline='') as f:
        json.dump({'2': todo_list}, f)
