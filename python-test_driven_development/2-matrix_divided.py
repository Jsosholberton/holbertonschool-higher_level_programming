#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """funcion that divides all elements
    Args:
        matrix (list): is a matrix of int or float values
        div (int): is a value for divide the elements in list

    Raises:
    ZeroDivisionError: if div is equal 0
    TypeError: matrix must be a list of lists of integers or floats
    TypeError: row of the matrix must be of the same size
    TypeError: div must be a number (integer or float)

    Return:
        div_matrix (list): All elements of the matrix divided by div,
        rounded to 2 decimal places
    """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_error)
    for index in matrix:
        if not isinstance(index, list) or len(index) == 0:
            raise TypeError(matrix_error)
        if len(index) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for must_number in index:
            if type(must_number) not in (int, float):
                raise TypeError(matrix_error)
    div_matrix = [[round(result / div, 2) for result in len] for len in matrix]

    return div_matrix
