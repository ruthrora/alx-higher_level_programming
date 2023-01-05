#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
    if last > 5:
        print("Last digit of {} is {}".format(number, last)
    elif last == 0:
        print("Last digit of {} is {}".format(number, last)
    else:
        print("Last digit of {} is {}".format(number, last)
