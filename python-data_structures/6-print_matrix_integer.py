#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j == len(matrix):
                    ended = ''
                else:
                    ended = ' '
                print('{}'.format(matrix[i][j]), end=ended)
            print()
