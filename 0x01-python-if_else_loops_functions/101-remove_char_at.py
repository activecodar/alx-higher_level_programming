#!/usr/bin/python3

def remove_char_at(str_, n):
    word = ""
    for c in range(0, len(str_)):
        word += str_[c] if c != n else ""
    return word
