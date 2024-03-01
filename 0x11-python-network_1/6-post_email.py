#!/usr/bin/python3
"""sends a POST request to the passed URL"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = {'email': email}
    req = requests.post(url, data=data)

    print(req.text)
