#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = [element % 2 == 0 for element in my_list]

    return new_list
