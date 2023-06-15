#!/usr/bin/python3
"""Definition of the method"""


def say_my_name(first_name, last_name=""):
    """
    Description.
    ------------

    Is a function that print two variables of name
    Args.
    ----

        first_name (str):
            Is the first name to print
        last_name (str):
            Is the last name to print

    Raises.
    ------
        TypeError:
            If first name or last name isn't str
    """

    if isinstance(first_name, str):
        print("My name is {:s}".format(first_name), end="")
    else:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str):
        print(" {:s}".format(last_name))
    elif last_name is not None:
        raise TypeError("last_name must be a string")
    else:
        print(" ")
