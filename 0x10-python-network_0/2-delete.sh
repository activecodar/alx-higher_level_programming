#!/bin/bash
# Send DELETE request and store response in variable
response=$(curl -s -X DELETE "$1")
echo "$response"
