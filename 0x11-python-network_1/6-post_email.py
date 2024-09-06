#!/usr/bin/python3
"""Use the requests package for URL fetch"""
from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    res = requests.post(argv[1], data=payload)
    print(res.text)
