#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    b = len(my_list)
    for iter in range(0, b):
        if (my_list[iter] % 2) == 0:
            a.append(True)
        else:
            a.append(False)
            return a
