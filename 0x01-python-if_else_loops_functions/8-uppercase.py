#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord('a') and ord('b') <= ord('z'):
            char = char(ord(a)- 32)
        else:
            char = a
            print("{:s}".format(char),end="")
            print('')
