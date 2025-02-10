#!/usr/bin/python3

"""
Module qui contient une fonction permettant d'enregistrer un objet Python
dans un fichier sous forme de chaine JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Enregistre un objet Python dans un fichier sous forme de chaine JSON.

    Args:
        my_obj (object): L'objet Python a enregistrer dans le fichier.
        filename (str): Le nom du fichier dans lequel enregistrer l'objet
                        au format JSON.

    Cette fonction utilise la fonction json.dump() pour convertir un objet
    Python en JSON et l'ecrire dans un fichier.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
