#!/usr/bin/python3

"""
Ce module contient une classe `CustomObject` avec les attributs suivants :
- `name` : une chaine de caracteres (le nom de la personne).
- `age` : un entier (l'age de la personne).
- `is_student` : un booleen (indiquant si la personne est etudiante).

La classe a deux methodes principales :
1. `serialize(self, filename)` : Cette methode permet de serialiser l'instance
de l'objet en un fichier binaire a l'aide du module `pickle`. Elle prend en
parametre un nom de fichier et sauvegarde l'objet dans ce fichier.
2. `deserialize(cls, filename)` : Cette methode de classe permet de
deserialiser un fichier binaire en un objet Python. Elle lit un fichier
specifie et renvoie l'objet deserialise.

Les exceptions sont gerees pour capturer les erreurs lors de la serialisation
et de la deserialisation, notamment pour les fichiers inexistants ou malformes
"""


import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Afficher les attributs de l'objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialiser l'objet courant et le sauvegarder dans un fichier."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialiser un objet depuis un fichier."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
