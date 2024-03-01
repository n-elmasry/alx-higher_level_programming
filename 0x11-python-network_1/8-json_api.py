#!/usr/bin/python3
"""uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=(username, password))
        data = response.json()
        print(data['id'])
    except Exception as err:
        print('None')
