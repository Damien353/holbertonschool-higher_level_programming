#!/usr/bin/python3

"""
Module qui contient une fonction permettant de lire un fichier texte (UTF-8)
et d'afficher son contenu dans la sortie standard.
"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et l'affiche dans la sortie standard.

    Args:
        filename (str): Le nom du fichier a lire. Par defaut, c'est une chaine vide,
                         ce qui entrainera une erreur si aucun fichier n'est fourni.

    Cette fonction utilise l'instruction 'with' pour garantir que le fichier est
    correctement ouvert et ferme apres la lecture de son contenu. Le contenu entier
    du fichier est ensuite affiche dans la sortie standard (stdout).
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
