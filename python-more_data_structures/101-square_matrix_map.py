#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda p_matr: list(map(lambda a: a**2, p_matr)), matrix))
