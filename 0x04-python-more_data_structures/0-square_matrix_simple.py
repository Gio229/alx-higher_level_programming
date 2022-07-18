#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareMatrix = []

    for line in matrix:
        squareMatrix.append([i**2 for i in line])
    return squareMatrix
