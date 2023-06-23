#!/usr/bin/python3
"""Definition of the function"""
import json


def from_json_string(my_str):
    """
    Description:
    -----------
       (Python data structure) represented by a JSON string:
    Args:
    -----
        my_str (str): the string to be converted
    Return:
    -------
        An object (Python data structure)
    """

    return json.loads(my_str)
