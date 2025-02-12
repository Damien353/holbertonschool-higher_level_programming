#!/usr/bin/python3

"""
Ce module contient deux fonctions :
1. serialize_and_save_to_file(data, filename) : Serialise un dictionnaire
Python et l'enregistre dans un fichier JSON.
2. load_and_deserialize(filename) : Charge un fichier JSON et le
convertit en dictionnaire Python.

Ces fonctions permettent de sauvegarder et recuperer des donnees en
utilisant le format JSON.
"""


import json

def serialize_and_save_to_file(data, filename):
    """Serialiser le dictionnaire et l'enregistrer dans un fichier JSON."""
    with open(filename, 'w') as file:
        # Serialiser le dictionnaire et ecrire dans le fichier
        json.dump(data, file)
    print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """Charger et deserialiser les donnees depuis un fichier JSON."""
    with open(filename, 'r') as file:
        # Deserialiser le contenu du fichier JSON en dictionnaire
        data = json.load(file)
    return data
