#!/usr/bin/python3

for i in range(0, 99):
    if i < 98:
        print("{:02}".format(i), end=", ")  # Affiche les nombres avec 2 chiffres, sauf pour 99
    else:
        print("{:02}".format(i)) #Pour afficher 99 sans ,
