#!/usr/bin/python3
import argparse
from calculator_1 import add, sub, mul, div


def calculate(args):
    matches = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return exit(1)
    a,o,b = int(args[0]), args[1], int(args[2])

    if o not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        return exit(1)
    else:
        res = matches[o](a, b)
        print("{:d} {} {:d} = {:d}".format(a, o, b, res))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('_args', nargs='*')
    args = parser.parse_args()._args
    calculate(args)
    
