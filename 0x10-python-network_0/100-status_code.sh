#!/bin/bash
# request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
