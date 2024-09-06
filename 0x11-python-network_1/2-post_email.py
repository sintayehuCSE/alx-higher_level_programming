#!/usr/bin/python3
"""POST an email to a URL"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = {'email': argv[2]}
    data = parse.urlencode(data).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
