#!/usr/bin/python3
def uppercase(str):
    for index in range(len(str)):
        if str[index] >= 'a' and str[index] <= 'z':
            tmp = ord(str[index]) - 32
            tmp = chr(tmp)
            str = str[:index] + tmp + str[index + 1:]
    print('{}'.format(str))
