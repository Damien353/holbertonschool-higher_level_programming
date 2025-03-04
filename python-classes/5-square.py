#!/usr/bin/python3
"""
Module: Square This module defines a Square class that represents a geometric
square. It allows manipulating square objects with a specified size. It offers
a property to access and modify the size, with validity checks. It also
provides methods to calculate the area of the square and display
a square made of #.

Class: Square: Represents a square with a size defined by an integer.
"""
class Square:
    """
    A class that defines a square by its size and provides methods
    to calculate its area and print its representation.
    """

    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Parameters:
        size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): The size of the square.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'. If the size is 0,
        prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            print('\n'.join([''.join('#' * self.__size)] * self.__size))
