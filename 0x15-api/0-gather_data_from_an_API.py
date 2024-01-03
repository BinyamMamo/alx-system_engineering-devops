#!/usr/bin/python3
""" gathers employee data form a REST api"""
from requests import get
from sys import argv

base_url = "base_url"
id = argv[1]
ename = ""
completed = []
tasks = 0

if __name__ == "__main__":
    with get(base_url + "/users/" + id) as response:
        response = response.json()
        ename = response["name"]

    with get(base_url + "/todos?userId=" + id) as response:
        response = response.json()
        for r in response:
            if (r['completed']):
                completed.append(r['title'])
            tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
                                ename, len(completed), tasks))
    for task in completed:
        print("\t{}".format(task))
