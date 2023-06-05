#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    arr_copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return arr_copy
    arr_copy[idx] = element
    return arr_copy
