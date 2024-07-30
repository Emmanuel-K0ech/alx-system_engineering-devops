#!/usr/bin/python3
""" Exports todo list information for a given employee ID to CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    # Fetch user data
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    # Fetch todos data
    todos = requests.get(base_url + "todos", params={
                        "userId": user_id}).json()
    # Write to csv file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write the header
        writer.writerow(["User ID", "Username", "Completed", "Title"])
        # Write each todo item
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])
