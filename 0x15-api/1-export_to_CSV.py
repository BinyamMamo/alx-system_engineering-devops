#!/usr/bin/python3
"""extracts a user's to-do list from a JSON API and saves it as a CSV file.
"""
import requests
from sys import argv
from csv import DictWriter, QUOTE_ALL


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
        "user_id" : uid,
        "username" : extract(f"users/{uid}")['username'],
        "status" : task['completed'],
        "title" : task['title']
    }
    todo_list.append(todo)

with open(f"{uid}.csv", 'w', newline='') as csv_file:
    fields = ["user_id", "username", "status", "title"]
    writer = DictWriter(csv_file, fieldnames=fields, quoting=QUOTE_ALL)
    writer.writerows(todo_list)
