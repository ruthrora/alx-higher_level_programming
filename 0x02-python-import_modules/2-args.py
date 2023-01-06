#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(sys.srgv) - 1
    if a == 0:
        print("{} argumants.".format(a))
    elif a == 1:
        print ("{} arguments:",format(a))
    else:
        print("{} arguments:".format(a))
        if a >= 1:
            a = 0
            for arg in sys.argv:
                if a != 0:
                    print("{}: {}".format(a, arg))
                    a += 1
