#!/usr/bin/python3
"""Function that print a square"""


def print_square(size):
    """
    Description:
        Print a square by a size
    -----------
    Args:
        size (int):
            Is the size of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
