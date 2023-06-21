#!/usr/bin/python3
"""Defition of the class inherits_from"""

def inherits_from(obj, a_class):
    """
    Description:
    -----------
        the object is an instance of a class that inherited?
    Args:
    -----
        obj (any):
        a_class (any):
    Return:
    -------
        True if the object is an instance of a class
        otherwise return False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
