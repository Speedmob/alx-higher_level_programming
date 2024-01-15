#!/usr/bin/python3
"""base model class"""
import json
import csv


class Base:
    """base for classes in almost a circle project

    Attributes:
        __nb_object (int): num of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a base instance.

        Args:
            id (int): id of base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON str representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON str representation of a list of objects to a file.

        Args:
            list_objs (list): list of instances that inherits from base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """a JSON string in a list.

        Args:
            json_string (str): A JSON str of a list of dicts.
        Returns:
            if JSON str is empty - empty list
            Otherwise - Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """an instance set with a dictionary of attributes.

        Args:
            **dictionary (dict): K/v pairs of attrs to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dum = cls(1, 1)
            else:
                dum = cls(1)
            dum.update(**dictionary)
            return dum

    @classmethod
    def load_from_file(cls):
        """a list of instances from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            if file does not exist - an empty list.
            Otherwise - a list of instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fn = ["id", "width", "height", "x", "y"]
                else:
                    fn = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fn=fn)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """a list of instances from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            if file does not exist - an empty list.
            Otherwise - a list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
