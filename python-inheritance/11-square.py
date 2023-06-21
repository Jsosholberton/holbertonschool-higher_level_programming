#!/usr/bin/python3
"""Definition of the class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of the subclass based in Rectangle"""

    def __init__(self, size):
        """
        Description:
        -----------
            method init

        Args:
        -----
            size (int): size of the Square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return:
        -------
            The area of the Square
        """
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
