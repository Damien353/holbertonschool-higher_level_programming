#!/usr/bin/python3

"""
This module defines a Rectangle class to represent a rectangle with 
specific attributes and methods for calculating area, perimeter, 
and string representation. The class includes property validation 
for the width and height attributes, keeps track of the number of 
Rectangle instances created, and supports a customizable symbol 
for the rectangle representation. It also includes a static method 
to compare the areas of two rectangles.
"""


class Rectangle:
    """
    A class to define a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for the string representation
        of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with optional width and height.
        
        Arguments:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        
        Increments the number_of_instances class attribute each time a new 
        Rectangle instance is created.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Arguments:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Arguments:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)) 
            or 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.

        Returns:
            str: A string containing the rectangle made of print_symbol 
            or an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)]
        )

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be 
        used to recreate it using eval.

        Returns:
            str: A string that represents the Rectangle object 
            in a format that can be evaluated.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted.

        This method also decrements the number_of_instances class 
        attribute each time an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles based on their area and returns the bigger one
        If both rectangles have the same area, rect_1 is returned.
        
        Arguments:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        
        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if
            areas are equal.
        
        Raises:
            TypeError: If rect_1 or rect_2 are not instances of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
