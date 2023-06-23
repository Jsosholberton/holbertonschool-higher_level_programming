#!/usr/bin/python3
"""Definition of the function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Description:
    ------------
        Save object to a json file
    Args:
    -----
        my_object (any): the object to be saved
    Return:
    -------
        The number of characttes written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(json.dumps(my_obj)))
