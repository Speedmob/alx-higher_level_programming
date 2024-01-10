#!/usr/bin/python3
"""a Student class file."""


class Student:
    """a student class."""

    def __init__(self, first_name, last_name, age):
        """creates a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets a dictionary representation of a Student.

        represents only attrs included in the list.

        Args:
            attrs (list): (Optional) attrs to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attrs of a Student.

        Args:
            json (dict): key/value pairs to replace attrs with.
        """
        for key, value in json.items():
            setattr(self, key, value)
