#!/usr/bin/python3
a = 89
b = 10
b = [a, b][0]
a = [b, a][0]
print("a={:d} - b={:d}".format(a, b))
