#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to retrieve information about a user's todo list progress.

Usage: ./0-gather_data_from_an_API.py [employee_id]
"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

employee_id = int(sys.argv[1])
base_url = "https://jsonplaceholder.typicode.com"
user_url = "{}/users/{}".format(base_url, employee_id)
todos_url = "{}/todos?userId={}".format(base_url, employee_id)

try:
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user = user_response.json()
except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))
    sys.exit(1)

try:
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()
except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))
    sys.exit(1)

total_tasks = len(todos)
done_tasks = sum(1 for t in todos if t['completed'])
employee_name = user['name']

print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))

for t in todos:
    if t['completed']:
        print("\t {}".format(t['title']))

