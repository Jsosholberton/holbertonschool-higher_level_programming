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
        """

        list_print = []
        name_to_save = cls.__name__ + ".json"

        if list_objs is not None:
            for index_obj in list_objs:
                list_print.append(index_obj.to_dictionary())

        string_rep = cls.to_json_string(list_print)
        with open(name_to_save, mode='w', encoding='utf-8') as file:
            file.write(string_rep)

    @staticmethod
    def from_json_string(json_string):
        """
        Description:
        ------------
            List of the JSON string representation
        Args:
        ----
            json_string (str): is a string representing a list of dictionaries
        Return:
        -------
            The list of the JSON string representation
            """

        if json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Description:
        ------------
            create a new instance with the same value
        Args:
        -----
            dictonary (dict): doble pointer to the dict work as a **kwargs
        Return:
        -------
            A new instance with the same value
        """
        """
        if cls.__name__ == "Rectangle":
            cls(1, 1) <--- Rectangle need 2 arguments to work
        else:
            cls(1) <--- Square need 1 argument to work
            The data inside the cls is any value >= 1 since we be update
            in the next line
        """

        dummy = cls(152, 351) if cls.__name__ == "Rectangle" else cls(400)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Description:
        ------------
            list of instances
        Args:
        -----
            cls: instance
        Return:
        -------
            a list of instances
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding='utf-8') as file:
                arr_dict = cls.from_json_string(file.read())
                list_instances = [cls.create(**dictonary) for dictonary in arr_dict]
                return list_instances
        except Exception:
            return []
