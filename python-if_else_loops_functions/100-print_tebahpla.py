#!/usr/bin/python3
for aBcD in range(122, 96, -2):
    tmp = chr(aBcD)
    upper = chr(aBcD - 1 - 32)
    print(f'{tmp}{upper}', end = "")
