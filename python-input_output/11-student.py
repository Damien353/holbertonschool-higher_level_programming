#!/usr/bin/python3
"""
Classe Student qui definit un etudiant avec un nom, un prenom et un age.
La methode to_json retourne une representation en dictionnaire de l'instance.
Si un parametre attrs est passe, seuls les attributs de cette liste
sont inclus. La methode reload_from_json permet de recharger un objet
avec des valeurs issues d'un dictionnaire.
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

    def to_json(self, attrs=None):
        """
        Retourne une representation en dictionnaire de l'objet Student.
        Si un parametre attrs est passe, seuls les attributs de cette
        liste sont inclus.
        
        Args:
            attrs (list, optional): Liste d'attributs a inclure dans
            le dictionnaire.

        Returns:
            dict: Le dictionnaire avec les attributs de l'etudiant.
        """
        if attrs is None:
            return self.__dict__

        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Recharge les attributs de l'objet Student a partir d'un
        dictionnaire json.

        Args:
            json (dict): Un dictionnaire avec les nouvelles valeurs pour
            les attributs.
        """
        for key, value in json.items():
            setattr(self, key, value)
