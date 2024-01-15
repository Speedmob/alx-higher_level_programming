#!/usr/bin/python3
"""a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square.

        Args:
            size (int): size of square.
            x (int): x coordinate of square.
            y (int): y coordinate of square.
            id (int): id of square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square.

        Args:
            *args (ints): attr values.
                - 1 id
                - 2 size
                - 3 x coordinate
                - 4 y coordinate
            **kwargs (dict): k/v of attr to replace attr with.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
