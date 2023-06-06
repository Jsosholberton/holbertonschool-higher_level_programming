#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dictionary = dict(a_dictionary)
    for key in mul_dictionary:
        mul_dictionary[key] = a_dictionary[key] * 2
    return mul_dictionary
