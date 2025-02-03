#!/usr/bin/python3
"""
Module contenant une fonction qui renvoie la liste des attributs et methodes
d'un objet donne. Cette fonction permet d'inspecter dynamiquement les
caracteristiques d'un objet sans avoir a connaitre sa structure interne.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et methodes disponibles d'un objet.
    Cette fonction utilise la fonction integree dir() pour obtenir la liste
    complete des attributs et methodes de l'objet, y compris ceux herites
    des classes parentes.
    Parameters:
        obj: objet dont on souhaite obtenir la liste des attributs et methodes
    Returns:
        list: Une liste contenant les noms des attributs et methodes de lobjet
    """
    return dir(obj)
