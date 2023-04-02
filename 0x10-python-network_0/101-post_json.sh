#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument
[ "$#" -lt 2 ] && echo "Usage: $0 <URL> <filename>" && exit 1 && curl -s -H "Content-Type: application/json" -d "@$2" -X POST "$1"
