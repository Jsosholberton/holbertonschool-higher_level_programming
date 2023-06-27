#!/usr/bin/python3
"""Definition of the class 'Base'"""
import json


class Base:
    """
    Description:
    ------------
        This is the base of the project
    Args:
    -----
        nb_objects (int): count num of objects, and set in id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
        -----------
            Definition of the class init
        Args:
        ----
            id (int): the id of the process?
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation of a string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Description:
        -----------
            Save a JSON file by a list
        Args:
        -----
            list_objs (list): list of objects to be saved
        Return:
        -------
            The file printed
        """

        list_printed = []
        name_to_save = cls.__name__ + ".json"
        if list_objs:
            for index_obj in list_objs:
                dict_obj_temp = index_obj.to_dictionary()
                list_printed.append(dict_obj_temp)
        string_rep = cls.to_json_string(list_printed)
        with open(name_to_save, mode='a', encoding='utf-8') as file:
            return file.write(string_rep)
