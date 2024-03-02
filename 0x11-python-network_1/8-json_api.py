#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ''

    req = requests.post(url, data={'q': q})

    try:
        data = req.json()
        if not data:
            print('No result')
        else:
            print(f"[{data.get('id')}] {data.get('name')}")

    except ValueError:
        print('Not a valid JSON')
