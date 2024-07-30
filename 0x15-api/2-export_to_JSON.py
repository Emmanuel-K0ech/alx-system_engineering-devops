#!/usr/bin/python3
""" Exports data to a file in JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(base_url).json()
    base_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todos = requests.get(base_url).json()
    name = user.get('username')
    x = [{"task": x.get("title"), "username": x.get("completed")}
         for x in todos]
    ftext = {}
    ftext[uid] = x
    with open("{}.json".format(uid), 'w')as filejs:
        json.dump(ftext, filejs)
