#!/usr/bin/env python3
from abc import ABC, abstractmethod

""" 
Classe abstraite Animal
Cette classe sert de base pour toutes les autres classes qui representent
des animaux. Elle contient une methode abstraite 'sound' qui doit etre
implemente par les classes derives.
"""
class Animal(ABC):
    
    @abstractmethod
    """ 
    Methode abstraite 'sound'
    Cette methode doit etre implemente par toutes les sous-classes d'Animal.
    Chaque sous-classe doit retourner le son caracteristique de l'animal.
    """
    def sound(self):
        pass

""" 
Sous-classe Dog
Cette classe herite de la classe Animal et implemente la methode 'sound'.
Elle retourne le son caracteristique du chien : 'Bark'.
"""
class Dog(Animal):
    
    def sound(self):
        """ Retourne le son d'un chien : 'Bark' """
        return "Bark"

""" 
Sous-classe Cat
Cette classe herite de la classe Animal et implemente la methode 'sound'.
Elle retourne le son caracteristique du chat : 'Meow'.
"""
class Cat(Animal):
    
    def sound(self):
        """ Retourne le son d'un chat : 'Meow' """
        return "Meow"

""" 
Test de la creation des objets
On cree une instance de chaque sous-classe et on appelle la methode
'sound' pour verifier le resultat.
"""
# Creation des objets
dog = Dog()
cat = Cat()

# Test de la methode sound
print(dog.sound())  # Affiche "Bark"
print(cat.sound())  # Affiche "Meow"
