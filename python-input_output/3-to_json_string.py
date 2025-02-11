#!/usr/bin/python3

"""
Module qui contient une fonction permettant de retourner la representation
JSON d'un objet Python sous forme de chaine de caracteres.
"""

import json


def to_json_string(my_obj):
    """
    Retourne la representation JSON d'un objet Python.

    Args:
        my_obj (object): L'objet Python a convertir en JSON.

    Retourne:
        str: La chaine JSON correspondant a l'objet fourni.

    Cette fonction utilise la fonction json.dumps() pour convertir un
    objet Python en une chaine JSON.
    """
    return json.dumps(my_obj)
