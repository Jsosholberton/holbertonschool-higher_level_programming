#!/usr/bin/python3
"""Definition of the function for read a file"""


def read_file(filename=""):
    """
    Description:
    ------------
        Read a file
    Args:
    -----
        filename (str): name of the file to be read
    """

    with open(filename, encoding='utf-8') as file_read:
        print(file_read.read(), end="")
