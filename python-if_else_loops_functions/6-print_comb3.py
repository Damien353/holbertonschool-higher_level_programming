#!/usr/bin/python3

for i in range(10):  # parcourt les chiffres de 0 a 9
    
    for j in range(i + 1, 10):  # parcourt chiffres plus grands que i
        
        if i == 8 and j == 9:  # si derniere combinaison
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
