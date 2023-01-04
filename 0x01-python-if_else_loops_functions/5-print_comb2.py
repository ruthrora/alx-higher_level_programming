#!/usr/bin/python3
for y in range(0, 100):
    if y == 99:
        print(y)
    else:
        print("{:0>2d}".format(y), end=",")
