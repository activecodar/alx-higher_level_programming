#!/bin/bash
#size of the response body and display it in bytes
curl -sI "$1" | awk '/Content-Length/ {print $2}'
