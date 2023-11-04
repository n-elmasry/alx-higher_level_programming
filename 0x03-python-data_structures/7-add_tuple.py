#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        firstNum = tuple_a[0]
        secondNum = tuple_a[1]
    elif len(tuple_a) == 1:
        firstNum = tuple_a[0]
        secondNum = 0
    else:
        firstNum = 0
        secondNum = 0

    if len(tuple_b) >= 2:
        firstNum += tuple_b[0]
        secondNum += tuple_b[1]
    elif len(tuple_b) == 1:
        firstNum += tuple_b[0]

    tuple_c = (firstNum, secondNum)
    return tuple_c
