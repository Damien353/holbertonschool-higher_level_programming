#!/usr/bin/python3
"""
Module: Square

This module defines a `Square` class that represents a square with
a defined size and position.
It allows you to create square objects, set and get their size and position
calculate their area, and print them in a specific format.

Classes:
    Square: A class to represent a square with a specified size and position.

Methods:
    __init__(size=0, position=(0, 0)): Initializes a new square with
    an optional size and position.
    size: Property to get and set the size of the square, with validation
    for non-negative integers. position: Property to get and set the position
    of the square, which must be a tuple of two non-negative integers.
    area(): Calculates and returns the area of the square.
    my_print(): Prints the square using `#` characters, with optional
    spacing based on the position.
"""


class Square:
    """
    A class to define a square with a size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with optional size and position.
        Parameters:
        size (int): The size of the square (default is 0).
        position (tuple): The position (x, y) to start printing the square
        (default is (0, 0)).
        """
        self.size = size
        self.position = position

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
        Sets the size of the square. Must be a non-negative integer.
        Parameters:
        value (int): The size of the square.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the current position of the square.
        Returns:
        tuple: The position (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square. Position must be a tuple of two positive integers.
        Parameters:
        value (tuple): A tuple representing the position (x, y).
        Raises:
        TypeError: If value is not a tuple of two integers.
        ValueError: If any integer is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
        int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'. If size is 0, prints an empty line.
        Position is used to add spaces before the square starts.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
