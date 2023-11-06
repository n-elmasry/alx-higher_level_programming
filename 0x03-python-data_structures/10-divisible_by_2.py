#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultList = []
    for num in my_list:
        if num < 0:
            return my_list
        elif num % 2 == 0:
            resultList.append(True)
        else:
            resultList.append(False)
    return resultList
