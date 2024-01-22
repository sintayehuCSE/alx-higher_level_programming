#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = "None"
    str_len = 0
    if sentence:
        str_len = len(sentence)
        first_char = sentence[0]
    pack_tuple = (str_len, first_char)
    return pack_tuple
