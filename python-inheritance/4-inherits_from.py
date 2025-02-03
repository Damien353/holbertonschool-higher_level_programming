#!/usr/bin/python3
"""
Module contenant une fonction qui renvoie True si l'objet est une 
instance d'une classe qui herite (directement ou indirectement) de la
classe specifiee sinon False.
"""


def inherits_from(obj, a_class):
    """
    Retourne True si objet est une instance d'une classe qui herite de a_class
    (directement ou indirectement), sinon False.
    Parameters:
        obj: L'objet que l'on souhaite tester.
        a_class: La classe a comparer.
    Returns:
        bool: True si obj est une instance d'une classe qui herite de a_class
              False sinon.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
