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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    """Return: his width"""
    return self.width


@property
def height(self):
    """Return: his height"""
    return self.height


@property
def x(self):
    """Return: his x"""
    return self.x


@property
def y(self):
    """Return: his y"""
    return self.y


@width.setter
def width(self, width):
    """Set the value for width"""
    self.width = width


@height.setter
def height(self, height):
    """Set the value for height"""
    self.height = height


@x.setter
def x(self, x):
    """Set the value for x"""
    self.x = x


@y.setter
def y(self, y):
    """Set the value for y"""
    self.y = y
