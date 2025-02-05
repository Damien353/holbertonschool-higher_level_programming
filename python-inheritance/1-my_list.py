#!/usr/bin/python3
"""
Module qui definit une classe MyList, qui herite de la classe de base list.
Cette classe ajoute une methode pour afficher la liste triée san
modifier l'originale.
"""


class MyList(list):
    """
    Classe qui herite de la classe liste et ajoute une methode
    pour imprimer la liste triee.
    """

    def print_sorted(self):
        """
        Imprime la liste triee par ordre croissant sans modifier
        la liste originale.
        """
        print(sorted(self))
