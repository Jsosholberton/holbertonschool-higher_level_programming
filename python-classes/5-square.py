#!/usr/bin/python3
"""Class Square defines a Square"""


class Square():
    """Class initiation for square"""
    def __init__(self, size=0):
        """Definition of the class Square, the value size
        must be an integer and >= 0
        Args:
            size (int): private attribute
        """
        self.__size = size
        if type(size) is not int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the self.__size to value, the value must be a
        integer and >= 0"""

        self.__size = value
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """Return area of the square"""
        return self.__size**2

    def my_print(self):

        """print the square using '#'"""
        for large in range(0, self.size):
            for index in range(0, self.size):
                print('#', end="")
            print()
