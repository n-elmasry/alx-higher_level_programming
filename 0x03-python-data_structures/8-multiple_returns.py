#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
     
    if len (sentence) == 0:
        firstCahr = None
    else:
        firstCahr = sentence[0]

    return(len1, firstCahr )
