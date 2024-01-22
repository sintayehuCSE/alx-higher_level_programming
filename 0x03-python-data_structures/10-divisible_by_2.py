#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_test = []
    if my_list:
        for intgr in my_list:
            if intgr % 2 == 0:
                divisible_test.append(True)
            else:
                divisible_test.append(False)
    return divisible_test
