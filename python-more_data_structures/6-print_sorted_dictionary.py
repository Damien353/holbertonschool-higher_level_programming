#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # tri cles dictionnaire dans ordre alphabet
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
