#!/usr/bin/python3
"""Definition of the class 'Base'"""


class Base:
    """
    Description:
    ------------
        This is the base of the project
    Args:
    -----
        nb_objects (int): count num of objects, and set in id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
        -----------
            Definition of the class init
        Args:
        ----
            id (int): the id of the process?
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
