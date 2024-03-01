#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    data = response.text

    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
