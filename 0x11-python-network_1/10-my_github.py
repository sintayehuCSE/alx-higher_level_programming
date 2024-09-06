#!/usr/bin/python3
"""Use the requests package for URL fetch"""
from sys import argv
import requests


if __name__ == "__main__":
    header = {'Accept': 'application/vnd.github+json',
              'Authorization': 'Bearer {}'.format(argv[2]),
              'X-GitHub-Api-Version': '2022-11-28'}
    url = "https://api.github.com/users/{}".format(argv[1])
    res = requests.get(url, headers=header)
    try:
        body = res.json()
        print(body.get('id'))
    except ValueError:
        pass
