#!/usr/bin/python3
class Square:
    """Defines a square by size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data.
        Args:
            size (int): value of the size
            position (tuple): position to print, two positive integers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter __size private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """getter __position private instance attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with # char"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for row in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __str__(self):
        str_list = []
        new_string = ""
        if self.size == 0:
            str_list.append('\n')
        else:
            for i in range(self.position[1]):
                str_list.append('\n')
            for row in range(self.size):
                for sps in range(self.position[0]):
                    str_list.append(' ')
                for c in range(self.size):
                    str_list.append('#')
                str_list.append('\n')
        return new_string.join(str_list[:-1])
