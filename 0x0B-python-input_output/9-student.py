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

    def to_json(self):
        """creates a dictionary representation of a Student."""
        return self.__dict__
