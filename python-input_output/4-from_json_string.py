#!/usr/bin/python3

"""
Module qui contient une fonction permettant de retourner un objet Python
repreente par une chaine JSON.
"""

import json


def from_json_string(my_str):
    """
    Retourne l'objet Python represente par une chaine JSON.

    Args:
        my_str (str): La chaine JSON a convertir en objet Python.

    Retourne:
        object: L'objet Python correspondant a la chaine JSON fournie.

    Cette fonction utilise la fonction json.loads() pour convertir une chaine
    JSON en un objet Python.
    """
    return json.loads(my_str)
