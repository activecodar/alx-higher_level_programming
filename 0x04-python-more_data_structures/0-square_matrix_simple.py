#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            squared[i][j] = matrix[i][j] ** 2
    return squared
