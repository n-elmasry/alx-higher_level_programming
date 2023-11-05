#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    if len1 == 0:
        firstChar = None
    else:
        firstChar = sentence[0]

    return len1, firstChar
