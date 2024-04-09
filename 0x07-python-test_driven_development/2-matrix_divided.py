#!/usr/bin/python3

"""Determining a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """ Divide all elements of matrix

    matrix(list): The list of intergers or float
    div(int/float): The Divisor
    Raises:
    TypeError: if the matrix receives a non number
    TypeError: if each row of the matrix is of not the same size
    TypeError: if div is not an int or float.
    ZeroDivisionError: If div is 0.
    Returns:
        A new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
