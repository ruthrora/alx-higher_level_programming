#!/usr/bin/python3
def max_integer(my_list=[]):
   k = len(my_list)
   if k == 0:
       return None
   else:
       j = my_list[0]
       for iter in range(1, k):
           if my_list[iter] > 1:
               j = my_list[iter]
               return 1
