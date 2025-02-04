#!/usr/bin/python3
"""
Module qui contient la classe Rectangle, qui herite de la classe BaseGeometry.
Cette classe permet de creer un rectangle en validant ses dimensions.
Elle inclut une methode pour calculer l'aire du rectangle et une
representation sous forme de chaine.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui herite de la classe BaseGeometry.
    Elle represente un rectangle et valide les dimensions de ce
    rectangle (largeur et hauteur).
    """

    def __init__(self, width, height):
        """
        Constructeur de la classe Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Leve:
            TypeError: Si la largeur ou la hauteur ne sont pas des entiers.
            ValueError: Si la largeur ou la hauteur sont inferieures ou
            egales a 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Retourne une representation en chaine du rectangle sous la forme
        "Rectangle(width, height)".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calcule l'aire du rectangle.

        Retourne:
            int: L'aire du rectangle (largeur * hauteur).
        """
        return self.__width * self.__height
