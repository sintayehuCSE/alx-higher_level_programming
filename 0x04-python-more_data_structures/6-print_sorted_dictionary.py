#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(list(a_dictionary.items())))
    for key, value in a_dictionary.items():
        print(key, end='')
        print(': ', end='')
        print(value)
