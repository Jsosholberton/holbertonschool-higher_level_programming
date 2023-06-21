#!/usr/bin/python3
"""Definition of the class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of the class Rectangle using the BaseGometry"""

    def __init__(self, width, height):
        """
        Description:
        -----------
            Use the Rectangle that inherits from BaseGeometry
        Args:
        ----
            width (int): the width of the rectangle
            height (int): the heigth of the rectable
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Description:
        ------------
            Modific the empty area to a real area
        Return:
        -------
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Description:
        ------------
            Description of the rectangle
        Return:
        -------
            Return the information of the rectangle
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
