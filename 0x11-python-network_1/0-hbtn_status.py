#!/usr/bin/python3
""" A Python script that fetches a resource from the internet"""
from urllib import request


if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
