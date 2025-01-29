#!/usr/bin/python3
"""
Module that defines a Rectangle class with width and height attributes,
methods for calculating area and perimeter, and a custom string
representation using `#`.
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height.

    This class has private attributes: width and height. It provides getter
    and setter methods for both attributes with proper validation.
    It also includes methods for calculating the area and perimeter of
    the rectangle, and a method for string representation
    using `#`, as well as a representation for recreating the instance with eval().
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with given width and height.

        Parameters:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Parameters:
            value (int): The width to be set.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Parameters:
            value (int): The height to be set.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
            
        If either width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using `#`.

        Returns:
            str: A string with the rectangle drawn using `#`. If width or
            height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string representation for debugging purposes,
        which can be used with eval() to recreate the instance.

        Returns:
            str: A string that can be used to recreate the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

