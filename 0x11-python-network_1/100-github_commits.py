#!/usr/bin/python3
"""
Displays 10 commits of the repository "rails" by the user "rail"
"""

import requests
from sys import argv

if __name__ == '__main__':
    repo = argv[1]
    owner = argv[1]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    r = requests.get(url)
    commits = r.json()

    for i in range(10):
        commit = commits[i]
        name = ((commit['commit'])['author'])['name']
        sha = commit['sha']
        print("{}: {}".format(sha, name))
