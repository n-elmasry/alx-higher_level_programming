import sys
""" solves the N queens problem. """

if not isinstance(N, int):
    print('N must be a number\n')
    exit(1)
elif N < 4:
    print('N must be at least 4')
    exit(1)
