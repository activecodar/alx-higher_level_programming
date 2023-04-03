#!/usr/bin/python3
"""
Module that fetches url passed in terminal
"""
import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.headers.get('X-Request-Id', None))
