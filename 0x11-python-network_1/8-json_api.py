#!/usr/bin/python3
"""
Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) == 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": query})
    try:
        res = response.json()
        print(f"[{res.get('id', None)}] {res.get('name', None)}") \
            if res else print("No result")
    except ValueError:
        print("Not a valid JSON")
