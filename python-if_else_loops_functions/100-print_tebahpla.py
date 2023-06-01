#!/usr/bin/python3
for aBcD in range(122, 96, -2):
    upper = aBcD - 1 - 32
    print("{}{}".format(chr(aBcD), chr(upper)), end="")
