#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    url = argv[1]
    with request.urlopen(url) as response:
        header = response.headers
        var = header.get('X-Request-Id')
        if var is not None:
            print(var)
