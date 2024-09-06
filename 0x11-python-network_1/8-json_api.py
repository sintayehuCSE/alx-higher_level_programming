#!/usr/bin/python3
"""Use the requests package for URL fetch"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ''}
    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        body = res.json()
    except (requests.exceptions.JSONDecodeError, ValueError):
        print("Not a valid JSON")
    else:
        if body:
            print("[{}] {}".format(body.get('id'), body.get('name')))
        else:
            print("No result")
