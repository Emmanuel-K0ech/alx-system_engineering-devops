#!/usr/bin/python3
""" A script to export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(base_url).json()
    base_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(base_url).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in todo:
            taskwriter.writerow([int(uid), user.get('username'),
                                 x.get('completed'),
                                 x.get('title')])
