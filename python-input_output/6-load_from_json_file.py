#!/usr/bin/python3

"""
Module qui contient une fonction permettant de charger un objet Python
a partir d'un fichier JSON.
"""

import json


def load_from_json_file(filename):
    """
    Charge un objet Python a partir d'un fichier JSON.

    Args:
        filename (str): Le nom du fichier a lire pour charger l'objet
                         au format JSON.

    Retourne:
        object: L'objet Python correspondant au contenu du fichier JSON.

    Cette fonction utilise la fonction json.load() pour lire un fichier JSON
    et convertir son contenu en un objet Python.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
