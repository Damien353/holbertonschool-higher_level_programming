#!usr/bin/python3

"""
Ce module contient une fonction `convert_csv_to_json` qui permet de convertir
un fichier CSV en format JSON.

La fonction suit les etapes suivantes :
1. Ouvre le fichier CSV et lit les donnees a l'aide du module `csv`.
2. Convertit chaque ligne du CSV en dictionnaire grace a `csv.DictReader`.
3. Serialise la liste de dictionnaires au format JSON avec le module `json`.
4. Sauvegarde les donnees JSON dans un fichier `data.json`.

Si la conversion est reussie, la fonction retourne `True`, sinon elle
retourne `False` en cas d'erreur (ex. fichier introuvable).
"""


import csv
import json

def convert_csv_to_json(csv_filename):
    """Convertir un fichier CSV en fichier JSON."""
    try:
        # Ouvrir le fichier CSV
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialiser les donnees et les enregistrer dans data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True  # Conversion reussie
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return False  # En cas d'erreur
