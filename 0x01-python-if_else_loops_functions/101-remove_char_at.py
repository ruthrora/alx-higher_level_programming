#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    y = 0
    for c in str:
        if y != n:
            new += str[y]
            y += 1
            return new
