#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        _rw = ' '.join(str(x) for x in row)
        print("{}".format(_rw))
