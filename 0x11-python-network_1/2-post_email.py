#!/usr/bin/python3
"""
Takes in a URL and email and sends a POST request to URL with email
as a parameter, then displays the response
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
