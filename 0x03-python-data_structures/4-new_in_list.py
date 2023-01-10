#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    i = len(my_list)
    if idx < 0 or idx >= i or i == 0:
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
