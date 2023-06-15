#!/usr/bin/python3
"""Function that print a text"""


def text_indentation(text):
    """
    Description:
    ------------
        Print a text, if any char are '. ? :'
        that print two new lines

    Args:
    -----
        text (str): Text to print must be str

    Raises:
    -------
        TypeError: text must be a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index in range(0, len(text)):
        print(text[index], end="")
        if text[index] in ('.', '?', ':'):
            print('\n')
    print()
