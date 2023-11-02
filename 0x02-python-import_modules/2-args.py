#!/usr/bin/python3
import sys


def print_arguments(arguments):
    num_args = len(arguments)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"1 argument:\n1: {arguments[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_arguments(arguments)
