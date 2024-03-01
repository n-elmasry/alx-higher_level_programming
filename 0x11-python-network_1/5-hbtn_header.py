#!/usr/bin/python3
""" displays the value of the variable X-Request-Id"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]

    response = requests.get(url)

    var = response.headers.get('X-Request-Id')

    if var is not None:
        print(var)
