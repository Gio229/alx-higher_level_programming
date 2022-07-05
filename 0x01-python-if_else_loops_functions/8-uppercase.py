#!/usr/bin/python3
def uppercase(str):
    cpt = 0
    length = len(str)
    for c in str:
        cpt += 1
        if ord(c) > 96 and ord(c) < 123:
            print(
                "{}".format(chr(ord(c) - 20)),
                end="\n" if (cpt == length) else ""
                )
        else:
            print(
                "{}".format(c),
                end="\n" if (cpt == length) else ""
                )
