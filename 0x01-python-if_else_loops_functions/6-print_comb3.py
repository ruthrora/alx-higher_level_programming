#!/usr/bin/python3
for m in range(0,9):
    for n in range(m + 1, 10):
        if m == 8:
            print("{}{}".format(m,n))
        else:
            print("{}{}".format(m,n), end=",")
