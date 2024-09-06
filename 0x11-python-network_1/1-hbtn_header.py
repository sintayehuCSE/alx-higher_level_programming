#!/usr/bin/python3
"""A scritp that takes in a URL, send a request to it and print
   out the value X-Request-Id header"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as res:
        print(res.headers.get("X-Request-Id"))
