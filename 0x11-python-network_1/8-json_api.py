#!/usr/bin/python3
"""
Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
