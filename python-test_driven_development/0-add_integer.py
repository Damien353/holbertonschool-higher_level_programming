#!/usr/bin/python3
"""
Module: This function is part of a simple calculation module
that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers, a and b. If a or b are floats, they are first 
    cast to integers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number, default is 98.

    Returns:
    int: The sum of a and b, both casted to integers.

    Raises:
    TypeError: If a or b are neither integers nor floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
