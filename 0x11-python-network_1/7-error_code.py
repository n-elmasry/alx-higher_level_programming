#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]

    respone = requests.get(url)
    print(respone.text)
    if respone.status_code >= 400:
        print(f'Error code: {response.status_code}')
