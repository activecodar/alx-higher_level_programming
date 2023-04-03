#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.content)}")
    print(f"\t- content: {response.content.decode('utf-8')}")
