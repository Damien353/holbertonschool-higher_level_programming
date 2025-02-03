#!/usr/bin/python3
"""
Module contenant une fonction qui renvoie True si l'objet est une instance de,
ou si l'objet est une instance d'une classe qui herite de, la classe specifiee
sinon False.
"""


def is_kind_of_class(obj, a_class):
    """
    Retourne True si l'objet est une instance de a_class ou si l'objet est une 
    instance d'une classe qui herite de a_class.
    Parameters:
        obj: L'objet que l'on souhaite tester.
        a_class: La classe a comparer.
    Returns:
        bool: True si obj est une instance de a_class ou une
              de ses sous-classes, False sinon.
    """
    return isinstance(obj, a_class)
