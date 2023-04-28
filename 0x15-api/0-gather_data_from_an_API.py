#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to retrieve information about a user's todo list progress.

Usage: ./0-gather_data_from_an_API.py [employee_id]
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
        todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))

        try:
            employee_name = user_response.json().get('name')
            todos = todos_response.json()
            total_tasks = len(todos)
            done_tasks = [t for t in todos if t.get('completed')]
            num_done_tasks = len(done_tasks)

            print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done_tasks, total_tasks))

            for task in done_tasks:
                print("\t {}".format(task.get('title')))
        except ValueError:
            print('Invalid JSON')
    else:
        print('Usage: ./0-gather_data_from_an_API.py [employee_id]')

