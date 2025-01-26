#!/usr/bin/python3
"""
This module contains a single function `say_my_name`
that prints a formatted message with a first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Alice")
        My name is Alice
        >>> say_my_name("Mike", last_name="Smith")
        My name is Mike Smith
        >>> say_my_name(123, "Doe")
        Traceback (most recent call last):
        ...
        TypeError: first_name must be a string
        >>> say_my_name("John", 456)
        Traceback (most recent call last):
        ...
        TypeError: last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
