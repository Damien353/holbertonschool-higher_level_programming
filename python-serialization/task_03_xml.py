#!/usr/bin/python3

"""
Ce module fournit des fonctions pour serialiser et deserialiser des donnees
Python au format XML.

1. `serialize_to_xml(dictionary, filename)` :
   Cette fonction prend un dictionnaire Python et un nom de fichier.
   Elle serialise le dictionnaire et sauvegarde les donnees dans un
   fichier XML. Chaque cle du dictionnaire devient une balise XML et chaque
   valeur devient le texte a l'interieur de la balise.

2. `deserialize_from_xml(filename)` :
   Cette fonction prend un nom de fichier XML, lit les donnees a partir du
   fichier et reconstruit un dictionnaire Python. Les balises XML deviennent
   des cles dans le dictionnaire et leurs contenus deviennent
   les valeurs associees.

Le module utilise la bibliotheque standard `xml.etree.ElementTree` pour
manipuler les fichiers XML.
"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialise un dictionnaire Python en un fichier XML.

    Arguments:
    dictionary -- Dictionnaire a serialiser.
    filename -- Nom du fichier ou l'XML sera sauvegarde.

    La structure XML generee sera sous forme de :
    <data>
        <key1>value1</key1>
        <key2>value2</key2>
        ...
    </data>
    """
    root = ET.Element("data")  # Creer l'element racine

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Creer un element pour chaque cle
        child.text = str(value)  # Convertir la valeur en chaine de caracteres

    tree = ET.ElementTree(root)  # Creer l'arbre XML
    tree.write(filename)  # Ecrire l'arbre XML dans le fichier

def deserialize_from_xml(filename):
    """
    Deserialise un fichier XML en un dictionnaire Python.

    Arguments:
    filename -- Nom du fichier XML a lire.

    Retourne:
    Un dictionnaire ou les balises XML sont les cles et leurs contenus
    sont les valeurs.
    """
    tree = ET.parse(filename)  # Parser le fichier XML
    root = tree.getroot()  # Recuperer l'element racine

    dictionary = {}
    for child in root:  # Parcourir les elements XML
        dictionary[child.tag] = child.text  # Ajouter chaque element

    return dictionary  # Retourner le dictionnaire
