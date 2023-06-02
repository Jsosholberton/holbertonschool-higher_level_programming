#!/usr/bin/python3
from sys import argv
size = len(argv) - 1
if size == 0:
    print("{} arguments.".format(size))
else:
    if size == 1:
        print("{} argument:".format(size))
    else:
        print("{} arguments:".format(size))
    for i in range(1, size + 1):
        print("{}: {}".format(i, argv[i]))
