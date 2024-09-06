#!/usr/bin/python3
"""Use the requests package for URL fetch"""
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: %s" % res.status_code)
    else:
        print(res.text)
