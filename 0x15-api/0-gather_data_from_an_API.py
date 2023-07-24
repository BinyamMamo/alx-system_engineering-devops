#!/usr/bin/python3
"""retrieves and displays the completed tasks of a user
    specified by their ID as an argument
"""
import requests
from sys import argv

def extract(end_point):
    """return the response object from the GET request
        made to the specified endpoint
    """
    base_uri = "https://jsonplaceholder.typicode.com/"
    return requests.get(base_uri + end_point).json()

if __name__ == "__main__":
    # user id received from the argument
    uid = argv[1]

    todos = extract(f"user/{uid}/todos")
    total = len(todos)

    todos = extract(f"user/{uid}" + f"/todos?completed=true")
    done = len(todos)

    user = extract(f"users/{uid}")
    employee_name = user['name']

    print("Employee", employee_name, f"is done with tasks({done}/{total}):")
    for task in todos:
        print("\t", task['title'])
