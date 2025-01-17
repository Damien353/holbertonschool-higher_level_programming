#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        # ve©rifier les multiples de 3 et 5 (FizzBuzz)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # ve©rifier les multiples de 3(Fizz)
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # ve©rifier les multiples de 5 (Buzz)
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # sinon imprime le nombre lui meme
        else:
            print("{}".format(i), end=" ")
