#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for y in range(len(str)):
        if y == n:
            continue
        else:
            newStr += str[y]
            return newstr
