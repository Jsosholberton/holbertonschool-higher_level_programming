#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    f_tuple = tuple_a + (0, 0)
    s_tuple = tuple_b + (0, 0)
    add_tuple = f_tuple[0] + s_tuple[0], f_tuple[1] + s_tuple[1]
    return add_tuple
