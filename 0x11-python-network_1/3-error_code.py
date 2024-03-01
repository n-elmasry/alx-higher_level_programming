#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
