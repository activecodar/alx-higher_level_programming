"""
Module for dividing all elements of a matrix.

This module provides a single function, `matrix_divided`,
which divides all elements of a matrix by a given number and
returns a new matrix.
If the input matrix is not a list of lists of integers or floats,
or if the divisor is not a number, a `TypeError` is raised.
If the divisor is 0,
a `ZeroDivisionError` is raised. If the rows of the matrix are not
of the same size,
a `ValueError` is raised. The elements of the new matrix are rounded to
2 decimal places.

Examples:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> div = 3
    >>> matrix_divided(matrix, div)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0], [2.33, 2.67, 3.0]]

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
      matrix: A list of lists of integers or floats.
      div: An integer or float.

    Raises:
      TypeError: If matrix is not a list of lists of integers
      or floats, or if div is not a number.
      ZeroDivisionError: If div is 0.
      ValueError: If the rows of matrix are not of the same size.

    Returns:
      A new matrix with all elements divided by div,
      rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix \
            (list of lists) of integers/floats')
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError('matrix must be a matrix\
             (list of lists) of integers/floats')

    # Check if rows of matrix are of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise ValueError('Each row of the matrix must have the same size')

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # Check if div is not 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
