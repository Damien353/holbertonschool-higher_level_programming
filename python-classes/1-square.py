#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size
"""

class Square:
    """
    This class defines a square by its size
    It has a private instance attribute 'size' that is initialized with the
    given value
    """
    
    def __init__(self, size):
        """
        Initializes the square with a given size

        Args:
            size (int or float): The size of the square
        """
        self.__size = size
