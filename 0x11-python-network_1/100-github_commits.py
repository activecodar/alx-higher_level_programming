#!/usr/bin/python3
"""
Script that takes 2 arguments in order to solve this challenge.
- The first argument will be the repository name
- The second argument will be the owner name
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/" \
          f"commits?per_page=10&page=1"
    response = requests.get(url)
    for commit in response.json():
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {name}")
