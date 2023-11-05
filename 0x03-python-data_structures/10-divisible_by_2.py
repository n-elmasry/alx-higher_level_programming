#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultList = []
    for num in my_list:
        if my_list[num] < 0:
            return my_list
        elif my_list[num] % 2 == 0:
            resultList.append(True)
        else:
            resultList.append(False)
    return resultList
