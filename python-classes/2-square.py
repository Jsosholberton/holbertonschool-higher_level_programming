#!/usr/bin/python3
"""Class Square that defines a square"""


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
