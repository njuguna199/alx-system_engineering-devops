#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python todo.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    sys.exit(1)

todos = response.json()

completed_tasks = [todo for todo in todos if todo["completed"]]
num_completed_tasks = len(completed_tasks)
num_total_tasks = len(todos)
employee_name = todos[0]["user"]["name"]

print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{num_total_tasks}):")

for task in completed_tasks:
    print(f"\t {task['title']}")

