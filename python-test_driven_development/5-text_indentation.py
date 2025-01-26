#!/usr/bin/python3
"""
This module provides a function to format text with two new lines
after specific punctuation marks: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Splits a text into lines with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If `text` is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I'm fine:")
        Hello.

        How are you?

        I'm fine:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

        result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".:?":
            result += "\n\n"
            i += 1           
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(result.strip(), end="")
