#!/usr/bin/python3
"""
This module provides a function to print a square with the character '#'.
"""


def print_square(size):

    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square (must be >= 0).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(2)
        ##
        ##

        >>> print_square(1)
        #

        >>> print_square(0)

        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0

        >>> print_square(3.5)
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
