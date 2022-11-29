#!/usr/bin/python3

def print_last_digit(number):
    number = 0 - number if number < 0 else number
    last = number % 10
    print("{}".format(last), end="")
    return last
