#!/usr/bin/python3
"""
Module qui contient la classe Square, qui herite de la classe Rectangle.
Cette classe permet de creer un carre avec une taille valide et
de calculer son aire.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui herite de la classe Rectangle.
    Elle represente un carre et valide la dimension de ce carre (taille).
    """

    def __init__(self, size):
        """
        Constructeur de la classe Square.

        Args:
            size (int): La taille du carre (largeur et hauteur).

        Leve:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inferieure ou egale a 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calcule l'aire du carre.

        Retourne:
            int: L'aire du carre (taille * taille).
        """
        return self.__size * self.__size
