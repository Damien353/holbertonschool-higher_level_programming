#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size
It validates the size parameter during instantiation and provides a method
to calculate the area
"""

class Square:
    """
    This class defines a square by its size
    It ensures that the size is an integer and greater than or equal to 0
    It also provides a method to calculate the area of the square
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

