#!/usr/bin/python3
"""Definition of the function"""
import json


def load_from_json_file(filename):
    """
    Description:
    -----------
        Crates an objext by a json file
    Args:
    -----
        filename (str): name of the file to be readed
    Return:
    -------
        an object by the json file
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
