#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = []
    for i in range(len(matrix)):
        l = []
        for j in range(len(matrix[i])):
            l.append(matrix[i][j]*matrix[i][j])
        new_m.append(l)
    return new_m
