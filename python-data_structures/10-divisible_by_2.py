#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible = [True if n % 2 == 0 else False for n in my_list]
    return divisible
