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
            x (int): The position of the rectangle in the eje X
            y (int): The position of the rectangle in the eje Y
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
        """Set the value for width
        Raises:
        -------
            TypeError if value is not int
            ValueError if values is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value for height
        Raises:
        -------
            TypeError if value is not int
            ValueError if values is <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value for x
        Raises:
        -------
            TypeError if value is not int
            ValueError if values is < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value for y
        Raises:
        -------
            TypeError if value is not int
            ValueError if values is < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return:
        ------
            The area of the rectanle
        """
        return self.__width * self.__height

    def display(self):
        """
        Description:
        ------------
            Print the representation of the rectangle using '#'
        """
        for y in range(self.__y):
            print()
        for index in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Description:
        -----------
            Prints the information of the rectangle
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Description:
        ------------
            Update the data of the rectangle attributes
        Args:
        -----
            args (list): list of arguments to be changed (needed in orden)
            kwargs (dict): Dictionary with the attributes to be changed (the
                           orden is not necesary)
        """

        if args:
            args_set = ['id', 'width', 'height', 'x', 'y']
            for index, value in enumerate(args):
                if index < len(args_set):
                    setattr(self, args_set[index], value)
        else:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return an dict of the attributes of the rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
