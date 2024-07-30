#!/usr/bin/python3
""" Exports data in JSON format """
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url).json()
    un_dict = {}
    u_dict = {}
    # Populate user dictionaries
    for user in users:
        uid = user.get("id")
        u_dict[uid] = []
        un_dict[uid] = user.get("username")
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todo_url).json()
    # Populate todo items for each user
    for x in todos:
        user_id = x.get("userId")
        u_dict[user_id].append({
            "task": x.get("title"),
            "completed": x.get("completed"),
            "username": un_dict.get(user_id)
        })
        # Write data to JSON file
        with open("todo_all_employees.json", 'w')as json_file:
            json.dump(u_dict, json_file, indent=4)
