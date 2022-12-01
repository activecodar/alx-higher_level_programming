#!/usr/bin/python3
import argparse


def output(args):
    sum_total = sum([int(i) for i in args])
    print("{:d}".format(sum_total))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('_args', nargs='*')
    args = parser.parse_args()._args
    output(args)
