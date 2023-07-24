#!/usr/bin/python3
"""retrieves and displays the completed tasks of a user
    specified by their ID as an argument
"""
import requests
import json


def extract(end_point):
    """return the response object from the GET request
        made to the specified endpoint
    """
    base_uri = "https://jsonplaceholder.typicode.com/"
    return requests.get(base_uri + end_point).json()

# current user's id
todo_dict = {}
users = extract("users")
for user in users:
    todo_list = []
    uid = user['id']
    todos = extract(f"user/{uid}/todos")
    for task in todos:
        todo = {
            "task" : task['title'],
            "completed" : task['completed'],
            "username" : user['username']
        }
        todo_list.append(todo)
    todo_dict[uid] = todo_list

with open("todo_all_employees.json", 'w', newline='') as f:
    json.dump(todo_dict, f)
