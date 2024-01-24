#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    store_key = []
    for keys in a_dictionary:
        if a_dictionary.get(keys) == value:
            store_key.append(keys)
    for key in store_key:
        del a_dictionary[key]
    return a_dictionary
