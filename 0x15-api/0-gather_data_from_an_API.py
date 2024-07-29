#!/usr/bin/python3
""" Returns infomation about and employees ToDo list """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <emloyee_id>".format(sys.argv[0]))
        sys.exit(1)
    # Base url for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos", params={
                        "userId": sys.argv[1]}).json()
    # Extracts the titles of completed tasks
    completed = [x.get("title") for x in todos if x.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
