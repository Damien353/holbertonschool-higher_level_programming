#!/usr/bin/python3
"""
Fonction qui retourne la description d'un objet sous forme de dictionnaire pour la serialisation en JSON.
Cette fonction extrait tous les attributs de l'objet, y compris les attributs prives (commencant par '__').
"""


def class_to_json(obj):
    """
    Retourne la description d'un objet sous forme de dictionnaire.

    Cette fonction prend un objet et retourne un dictionnaire contenant tous ses attributs.
    Les attributs prives (commencant par '__') sont inclus.

    Args:
        obj: L'objet dont on veut obtenir la description sous forme de dictionnaire.

    Returns:
        dict: Un dictionnaire contenant les attributs de l'objet.
    """
    return obj.__dict__
