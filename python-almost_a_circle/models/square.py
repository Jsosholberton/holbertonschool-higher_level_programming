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
        """"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Property getter"""
        return self.size

    @size.setter
    def size(self, size):
        """Property setter"""
        self.height = size
        self.width = size

    def __str__(self):
        """
        Description:
        -----------
            Prints the information of the Square
        """
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                self.x, self.y, self.width))
