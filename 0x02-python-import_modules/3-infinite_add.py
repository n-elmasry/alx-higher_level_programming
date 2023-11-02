#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
arg_sum = 0

for arg in arguments:
    arg_sum += int(arg)
print(arg_sum)

