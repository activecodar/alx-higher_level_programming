#!/bin/bash
# Send request and get the size of the response body
response=$(curl -sI "$1")
size=$(echo "$response" | awk '/Content-Length/ {print $2}')

# Display the size of the response body in bytes
echo "${size}"
