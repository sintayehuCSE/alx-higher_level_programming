#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    big = {}
    for key in a_dictionary:
        lst = [(key, a_dictionary[key])]
        if not big:
            big.update(lst)
            continue
        for ky in big:
            if a_dictionary[key] > big[ky]:
                big.clear()
                big.update(lst)
    key = str(list(big.keys())[0])
    return key
