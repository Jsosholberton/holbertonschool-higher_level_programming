#!/usr/bin/python3
"""Class Student"""


class Student:
    """Definition of the class"""

    def __init__(self, first_name, last_name, age):
        """
        Args:
        -----
            first_name (str): value first name
            last_name (str): value last name
            age (int): value of the age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary with simple data structure"""

        return self.__dict__
