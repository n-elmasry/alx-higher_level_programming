#!/usr/bin/python3
""" sends a POST request to the passed URL"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    # encode the email
    data = parse.urlencode({'email': email}).encode()

    req = request.Request(url, data=data, method='POST')

    with request.urlopen(req) as response:
        data = response.read().decode('utf-8')

    print(data)
