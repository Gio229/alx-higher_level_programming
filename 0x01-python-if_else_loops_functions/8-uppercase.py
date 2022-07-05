#!/usr/bin/python3
def uppercase(str):
    cpt = 0
    length = len(str)
    for c in str:
        cpt += 1
        if ord(c) > 96 and ord(c) < 123:
            if cpt == length:
                print("{}".format(chr(ord(c) - 20)))
            else:
                print("{}".format(chr(ord(c) - 20)), end='')
        else:
            if cpt == length:
                print("{}".format(c))
            else:
                print("{}".format(c), end='')
