#!/usr/bin/python3
"""Documentation for rectangle class"""


from models.base import Base


class Rectangle(Base):

    """Rectangle class which inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id (int): the id of the rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of the width attribute
        Returns:
            the width of the instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute
        Args:
            value (int): value to set to width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute
        Returns:
            the height of the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute
        Args:
            value (int): the value to set the height to
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute
        Returns:
            the x attribute of the instance
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute
        Args:
            value (int): the value to set the x attribute to
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute
        Returns:
            the y attribute of the instance
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the y attribute
        Args:
            value (int): the value to set the y attribute to
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle instance
        Returns:
            the area of the current rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """Displays the rectangle with a # sign
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Overloads the __str__ method to print specific syntax"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes in a list *args or **kwargs
        Args:
            *args (list): non-keyworded argument list
            **kwargs (dict): keyworded argument list
        """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.width = kwargs['width']
                    if i == 'height':
                        self.height = kwargs['height']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """Returns a dictionary representation of the object
        Returns:
            a dictionary containing the attributes of the object
        """

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
