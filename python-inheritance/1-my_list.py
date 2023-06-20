#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """
    Descrption:
    -----------
        That prints the list, but sorted (ascending sort)
    Args:
    -----
        list (list): the list to be printed sorted
    """

    def print_sorted(self):
        print(sorted(self))
