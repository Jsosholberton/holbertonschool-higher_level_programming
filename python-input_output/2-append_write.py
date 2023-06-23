#!/usr/bin/python3
"""Definition of the function"""


def append_write(filename="", text=""):
    """
    Description:
    ------------
        Write into a file
    Args:
    ----
        filename (str): name of the file
        text (str): the text into the file
    Return:
        The number of characters written
    """

    with open(filename, mode='a', encoding='utf-8') as file:
        return (file.write(text))
