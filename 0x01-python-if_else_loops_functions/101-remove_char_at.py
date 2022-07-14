#!/usr/bin/python3
def remove_char_at(str, n):
    str_r = ""
    for letter in str:
        if n >= len(str) or n < 0:
            str_r = str
            break
        elif letter == str[n]:
            continue
        else:
            str_r += letter
    return str_r
