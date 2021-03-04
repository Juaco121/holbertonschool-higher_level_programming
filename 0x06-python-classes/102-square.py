#!/usr/bin/python3
class Square:
    """Defines a square by size."""
    def __init__(self, size=0):
        """Initializes the data.
        Args:
            size (int): value of the size
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter __size private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ge__(self, other):
        return self.size >= other.size
