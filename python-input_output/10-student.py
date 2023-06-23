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

    def to_json(self, attrs=None):
        """Return dictionary with simple data structure"""
        if isinstance(attrs, list) and ([isinstance(n, str)] for n in attrs):
            new_dict = {}
            for words in attrs:
                if words in self.__dict__:
                    new_dict[words] = self.__dict__[words]
            return new_dict

        return self.__dict__
