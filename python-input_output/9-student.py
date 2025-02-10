#!/usr/bin/python3
"""
Classe Student qui definit un etudiant avec un nom, un prenom et un age.
La methode to_json retourne une representation en dictionnaire de l'instance.
"""


class Student:
    """
    Classe qui definit un etudiant avec les attributs :
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructeur de la classe Student.

        Args:
            first_name (str): Le prenom de l'etudiant.
            last_name (str): Le nom de l'etudiant.
            age (int): L'age de l'etudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne une representation en dictionnaire de l'objet Student.

        Returns:
            dict: Le dictionnaire avec les attributs de l'etudiant.
        """
        return self.__dict__
