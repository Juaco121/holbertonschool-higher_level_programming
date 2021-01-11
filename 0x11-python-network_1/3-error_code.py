#!/usr/bin/python3
"""
Sends a request to the URL and manages HTTP error exceptions"
"""

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
