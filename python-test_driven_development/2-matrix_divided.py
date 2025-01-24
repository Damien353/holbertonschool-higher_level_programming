#!/usr/bin/python3
"""
Module for matrix operations.

This module contains a function to divide all elements of a matrix by a given
divisor. The function handles input validation and returns a new matrix with
results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number (div), and returns a new
    matrix.

    Parameters:
    matrix (list of lists): A matrix (list of lists) containing integers or
                             floats.
    div (int or float): The divisor, which must be a number and not zero.

    Returns:
    list of lists: A new matrix with each element divided by div, rounded to
                   2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the matrix does not have the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if not all(isinstance(item, (int, float)) for row in matrix
               for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
