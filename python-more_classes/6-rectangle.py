#!/usr/bin/python3

"""
This module defines a Rectangle class to represent a rectangle with
specific attributes and methods for calculating area, perimeter,
and string representation. The class includes property validation
for the width and height attributes and keeps track of the number
of Rectangle instances created. The module handles the following:

- Width and height validation with appropriate error handling
- Calculation of the rectangle's area and perimeter
- Custom string representation for printing and recreating the object
- Destructor that prints a message when an instance is deleted
"""


class Rectangle:
    """
    A class to define a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with optional width and height.
        
        Arguments:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle, with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle, with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle, printed with #.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Return a string that can be used to recreate the rectangle with eval.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
