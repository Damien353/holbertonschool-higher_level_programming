#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # utilise comprehension de liste pour creer new matrix
    return [[x ** 2 for x in row] for row in matrix]
