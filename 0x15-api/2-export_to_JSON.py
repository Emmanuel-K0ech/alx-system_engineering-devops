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
    todo = requests.get(base_url).json()
    name = user.get('username')
    t = [{"task": t.get("title"),
          "username": name,
          "completed": t.get("completed")} for t in todo]
    jb = {}
    jb[uid] = t
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(jb, filejs)
