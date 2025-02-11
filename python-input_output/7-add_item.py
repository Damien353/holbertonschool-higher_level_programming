#!/usr/bin/python3
"""
Script pour ajouter tous les arguments a une liste Python et les sauvegarder dans un fichier.

Ce script utilise les fonctions 'save_to_json_file' et 'load_from_json_file'
pour gerer la liste des arguments. La liste est sauvegardee dans un fichier JSON
nomme 'add_item.json'. Si le fichier n'existe pas, il est cree.
"""

import sys
import json
save_to_json_file = __import__('5-save_from_json_file')
load_from_json_file = __import__('6-load_from_json_file')


def add_items():
    """
    Ajoute tous les arguments de la ligne de commande a une liste et la sauvegarde dans un fichier JSON.

    Cette fonction :
    - Charge la liste existante depuis le fichier JSON (si elle existe).
    - Ajoute tous les nouveaux arguments de la ligne de commande a la liste.
    - Sauvegarde la liste mise a jour dans le fichier JSON.
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
