#!/usr/bin/python3
"""Class Square defines a Square"""


class Square():
    """Class initiation for square"""
    def __init__(self, size=0, position=(0, 0)):
        """Definition of the class Square, the value size
        must be an integer >= 0
        Args:
            size (int): private attribute
            position (tuple): private attributte
        """

        self.__position = position
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set the self.__size to value, the value must be a
        integer and >= 0"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of the square"""

        return self.__size**self.__size

    def my_print(self):
        """print the square using '#'"""

        if self.size == 0:
            print()
        else:
            for height in range(self.position[1]):
                print()
            for large in range(self.size):
                for space in range(self.position[0]):
                    print(" ", end="")
                for index in range(self.size):
                    print('#', end="")
                print()

    @property
    def position(self):
        """Return the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the self.__size to value, the value must be a
        integer and >= 0"""
        if isinstance(value, tuple) is False or len(value) != 2\
                or isinstance(value[0], int) is False\
                or isinstance(value[1], int) is False\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
