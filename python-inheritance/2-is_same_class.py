#!/usr/bin/python3
"""
Module contenant une fonction qui renvoie True si l'objet est exactement une 
instance de la classe specifiee, sinon False.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instance de la classe a_class.
    Parameters:
        obj: L'objet que l'on souhaite tester.
        a_class: La classe a comparer.
    Returns:
        bool: True si obj est une instance exacte de a_class, False sinon.
    """
    return type(obj) == a_class
