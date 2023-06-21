#!/usr/bin/python3
"""Definition of the class is_kind_class"""


def is_kind_of_class(obj, a_class):
    """
    Description:
    ------------
        The object is an instance of?
    Args:
    -----
        obj (any): object to be comparate
        a_class (any): class to be comparate with the objet
    Return:
    -------
        True if the object is a instance of the class
        otherwise False.
    """

    return isinstance(obj, a_class)
