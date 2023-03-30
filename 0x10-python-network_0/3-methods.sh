#!/bin/bash
curl -sI $1 | grep 'Allow' | awk '{print $2}'
