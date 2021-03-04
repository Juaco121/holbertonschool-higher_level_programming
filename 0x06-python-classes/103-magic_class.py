#!/usr/bin/python3
import math


class MagicClass:
    """MagicClass function
    Args: radius (int or float)
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """return the area of the object"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """return the circunference of the object"""
        return 2 * math.pi * self.__radius
