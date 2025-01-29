#!/usr/bin/python3
"""
Module that defines a Rectangle class with width and height attributes.

This module contains the definition of the Rectangle class, which has private
instance attributes: width and height.It includes property getters and setters
with validation to ensure that the attributes are positive integers.
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height.

    This class has private attributes: width and height.
    It provides getter and setter methods for both attributes with
    proper validation to ensure they are positive integers.
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
