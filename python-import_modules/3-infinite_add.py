#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv)
    result = 0
    for i in range(1, size):
        result += int(argv[i])
    print('{}'.format(result))
