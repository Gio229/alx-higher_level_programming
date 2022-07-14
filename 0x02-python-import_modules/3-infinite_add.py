#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    length = len(sys.argv)
    if (length <= 1):
        print("{}".format(sum))
    else:
        for number in range(1, length):
            sum += int(sys.argv[number])
        print("{}".format(sum))
