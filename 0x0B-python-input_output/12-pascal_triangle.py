#!/usr/bin/python3
"""
Module for Pascal's triangle calculation
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
        n (int): number of rows

    Returns:
        list: list of lists of integers
              representing the Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j-1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
