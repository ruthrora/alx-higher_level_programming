#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        char = ord(str[a])
        if char >= 97 and char <= 122:
            char = char -32
            print("{}".format(chr(chr)),end="")
            print()
