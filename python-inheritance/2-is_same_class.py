#!/usr/bin/python3
""" Definition of the class is_same_class"""


def is_same_class(obj, a_class):
    """
    Description:
    ------------
        Exact same object
    Args:
    -----
        obj (any): the value for be comparate his value
        a_class (any): the type for be comparate
    Return:
    -------
        True: if if the object is exactly an instance of the specified class
        Otherwise False.
    """

    return type(obj) == a_class
