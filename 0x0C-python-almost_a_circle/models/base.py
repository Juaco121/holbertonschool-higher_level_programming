#!/usr/bin/python3
"""Documentation for Base class"""


import os
import json


class Base:

    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation function for Base instance
        Args:
            id (int): the id of the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries
        Args:
            list_dictionaries (list): the list of dictionaries
        Returns:
            the JSON representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file
        Args:
            list_objs (list): list of instances who inherits from Base
        """

        list_objects = []
        if list_objs is None or len(list_objs) is 0:
            list_objects = []
        else:
            for i in list_objs:
                list_objects.append(i.to_dictionary())
        json_string = Base.to_json_string(list_objects)
        with open("{}.json".format(cls.__name__), mode='w', encoding='utf-8')\
                as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation argument
        Args:
            json_string (str): the JSON object representation of a list
            of dictionaries
        """

        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary of attributes to set
        Returns:
            the instance with all attributes set
        """

        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            new_base = cls(1, 1)
        if cls == Square:
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file with JSON object
        Returns:
            the instance list object with all instances initialized
        """

        instance_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as f:
                instance_object = cls.from_json_string(f.read())
                for instance_dict in instance_object:
                    instance_list.append(cls.create(**instance_dict))
                return instance_list
        else:
            return []
