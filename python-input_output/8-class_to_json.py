#!/usr/bin/python3
"""Definition of the function"""


def class_to_json(obj):
    """
    Description:
    ------------
        Dictionary description with simple data structure
    Args:
    ----
        obj (any): objext to be transform
    Return:
    -------
        Dictionary with simple data structure
    """

    return obj.__dict__
