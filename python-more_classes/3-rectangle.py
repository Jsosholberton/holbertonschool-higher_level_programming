#!/usr/bin/python3
"""Class that define a Rectangle"""


class Rectangle:
    """
    Description:
    -----------
        principal class that defines a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Description:
        ------------
            Initialitation of the args
        Args:
        ----
            width (int): first size
            height (int): second size
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Return:
        -------
            The value width
        """
        return self.__width

    @property
    def height(self):
        """
        Return:
        ------
            The value height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Description:
        -----------
            Set a value for the width variable
        Args:
        -----
            value (int): value to set into width
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Description:
        -----------
            Set a value for the height variable
        Args:
        -----
            value (int): value to set into height
        Raises:
        -------
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Return:
        -------
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return:
        -------
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Description:
        -----------
            Creates a string that represent a rectangle
        Return:
        -------
            Ordenated string to be printed
        """

        str_to_print = ""
        if self.__height == 0 or self.__width == 0:
            return str_to_print

        for index in range(self.__height):
            for index_2 in range(self.__width):
                str_to_print += "#"
            if index < self.__height - 1:
                str_to_print += "\n"
        return str_to_print
