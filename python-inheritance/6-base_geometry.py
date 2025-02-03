#!/usr/bin/python3
"""
Module contenant la classe BaseGeometry avec une methode
area() non implementee.
"""


class BaseGeometry:
    """
    Classe de base pour la geometrie.
    """

    def area(self):
        """
        Leve une exception pour indiquer que la methode area()
        n'est pas implementee.
        """
        raise Exception("area() is not implemented")
