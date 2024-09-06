#!/usr/bin/python3
"""Use the requests package for URL fetch"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = requests.get(url)
    try:
        body = res.json()
        for i in range(10):
            commit = body[i]
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except (ValueError, KeyError, IndexError):
        pass
