#!/usr/bin/python3
"""Prototype add two integers"""


def add_integer(a, b=98):
    """Adds two integer or floats a + b

    Args:
        a (int or float): first value
        b (int or float): second value

    Raises:
        TypeError: values must be integer

    Return:
        an integer the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a + b)
