#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

url = "https://alx-intranet.hbtn.io/status"
with request.urlopen(url) as response:
    data = response.read()

print('Body response:')
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data.decode('utf-8')))
