#!/usr/bin/python3
"""Definition of the class 'Rectangle' by Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Description:
    ------------
        Definition of the class Square by Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Description:
        ------------
            Definition of init method
        Args:
        -----
            size (int): the square size
            x (int): The position of the square in the eje X
            y (int): The position of the square in the eje Y
            id (int): id of the proccess
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Return: his size using width"""
        return self.width

    @size.setter
    def size(self, size):
        """Set the size in width and height"""
        self.width = size
        self.height = size

    def __str__(self):
        """
        Description:
        -----------
            Prints the information of the Square
        """
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                self.x, self.y, self.width))
