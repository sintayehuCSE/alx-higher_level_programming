#!/usr/bin/python3
"""A script that make URL request while handling exceptions"""
from sys import argv
from urllib import request
from urllib.error import HTTPError


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
