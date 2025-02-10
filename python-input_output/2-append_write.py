#!/usr/bin/python3

"""
Module qui contient une fonction permettant d'ajouter une chaine de caracteres
a la fin d'un fichier texte (UTF-8) et de retourner le nombre de caracteres ajoutes.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaine de caracteres a la fin d'un fichier texte (UTF-8) et retourne
    le nombre de caracteres ajoutes.

    Args:
        filename (str): Le nom du fichier dans lequel ajouter le texte. Si le fichier
                         n'existe pas, il sera cree.
        text (str): La chaine de caracteres a ajouter a la fin du fichier.

    Retourne:
        int: Le nombre de caracteres ajoutes dans le fichier.

    Cette fonction ouvre le fichier en mode ajout (ce qui cree le fichier s'il n'existe
    pas), ajoute la chaine de caracteres fournie et retourne le nombre de caracteres ajoutes.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
