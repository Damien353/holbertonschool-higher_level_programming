#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size,
a getter and setter for size, and a method to calculate the area
"""

class Square:
    """
    This class defines a square by its size, validates the size attribute,
    and provides a method to calculate the area
    """
    
    def __init__(self, size=0):
        """
        Initializes the square with a given size

        Args:
            size (int, optional): The size of the square. Defaults to 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size  # This will use the setter

    @property
    def size(self):
        """
        Retrieves the current size of the square
        
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring that it is an integer
        and greater than or equal to 0
        
        Args:
            value (int): The size of the square
        
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size
