#!/usr/bin/python3
"""Definition of the function"""
import json


def to_json_string(my_obj):
    """
    Description:
    -----------
       JSON representation of a string
    Args:
    -----
        my_obj (str): the string to be converted
    Return:
    -------
        The JSON representation of a string
    """

    return json.dumps(my_obj)
