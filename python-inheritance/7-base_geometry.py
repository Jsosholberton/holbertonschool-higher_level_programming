#!/usr/bin/python3
"""Definition of the class"""


class BaseGeometry:
    """
    Description:
    ------------
        Empty class
    """

    def area(self):
        """
        Raises:
        ------
            Area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Description:
        -----------
            Checks if the value is an intenger
        Args:
        -----
            name (str): name of the value
            value (int): value to be check
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
