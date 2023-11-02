#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    arg_sum = 0

    for arg in arguments:
        arg_sum += int(arg)
    print(arg_sum)
