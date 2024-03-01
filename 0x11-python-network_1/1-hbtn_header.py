#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
from urllib import request
from sys import argv

url = argv[1]

with request.urlopen(url) as response:
    header = response.headers
    if 'X-Request-Id' in header:
        print(header['X-Request-Id'])
