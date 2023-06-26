#!/usr/bin/python3
"""Definition of the class 'Rectangle' by Base"""
from models.base import Base


class Rectangle(Base):
    """
    Description:
    ------------
        Definition of the class Rectangle by Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Description:
        ------------
            Definition of init method
        Args:
        -----
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): any
            y (int): any
            id (int): id of the proccess?
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return: his width"""
        return self.__width

    @property
    def height(self):
        """Return: his height"""
        return self.__height

    @property
    def x(self):
        """Return: his x"""
        return self.__x

    @property
    def y(self):
        """Return: his y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
