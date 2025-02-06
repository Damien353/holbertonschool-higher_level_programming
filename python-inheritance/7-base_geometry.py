#!/usr/bin/python3
"""
Module qui contient la classe BaseGeometry.
Cette classe fournit des operations geometriques de base, telles que la
validation d'entiers et la gestion des erreurs liees au calcul d'aires.
Elle est destinee a etre etendue par d'autres classes qui implementent
des formes geometriques plus specifiquees.
"""


class BaseGeometry:
    """
    Ceci est une classe de base pour la geometrie.
    Elle fournit des operations geometriques de base qui peuvent etre heritees
    par d'autres formes geometriques.
    """

    def area(self):
        """
        Methode qui leve une exception si elle est appelee, car le calcul
        de l'aire n'est pas implemente dans la classe de base.

        Leve:
            Exception: avec le message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier positif.
        
        Args:
            name (str): Le nom du parametre a valider.
            value (int): La valeur a valider.
        Leve:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inferieure ou egale a 0
            
        La methode s'assure que la valeur passee est un entier 
        superieur a 0, en levant les exceptions appropriees en cas d'echec
        de la validation.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
