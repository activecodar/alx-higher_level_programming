#!/usr/bin/python3
import argparse


def output(args, plural=False):
    plural_letter = 's' if plural else ''
    if len(args) == 0:
        print("{:d} argument{}.".format(len(args), plural_letter))
    else:
        print("{:d} argument{}:".format(len(args), plural_letter))
        for idx, arg in enumerate(args):
            print("{:d}: {}".format(idx + 1, arg))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('_args', nargs='*')
    args = parser.parse_args()._args
    output(args, plural=len(args) != 1)
