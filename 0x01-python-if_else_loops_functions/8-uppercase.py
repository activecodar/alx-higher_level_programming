#!/usr/bin/python3

def uppercase(str_):
    word = ""
    for c in str_:
        if 96 < ord(c) < 123:
            word += chr(ord(c) - 32)
        else:
            word += c
    print("{}".format(word))
