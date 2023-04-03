#!/usr/bin/python3
"""
Module that fetches data using the urllib package
"""
import urllib.request

if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(URL) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
