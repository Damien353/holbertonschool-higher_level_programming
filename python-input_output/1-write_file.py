#!/usr/bin/python3

"""
Module qui contient une fonction permettant d'ecrire une chaine de caracteres
dans un fichier texte (UTF-8) et de retourner le nombre de caracteres ecrits.
"""


def write_file(filename="", text=""):
    """
    Ecrit une chaine de caracteres dans un fichier texte (UTF-8) et retourne
    le nombre de caracteres ecrits.

    Args:
        filename (str): Le nom du fichier dans lequel ecrire. Si le fichier
                         n'existe pas, il sera cree.
        text (str): La chaine de caracteres a ecrire dans le fichier.

    Retourne:
        int: Le nombre de caracteres ecrits dans le fichier.

    Cette fonction ouvre le fichier en mode ecriture (ce qui ecrase le contenu
    s'il existe), ecrit la chaine de caracteres fournie et retourne le nombre
    de caracteres ecrits.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
