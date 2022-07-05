#!/usr/bin/python3
def print_last_digit(number):
    val = number % 10 if number > 0 else (-1 * number) % 10
    print("{}".format(val), end='')
    return val
