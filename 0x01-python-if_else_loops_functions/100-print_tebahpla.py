#!/usr/bin/python3
def reverse_ASCII_alphabet_and_mix_case_alternatively():
    i = 1
    for char in range(-90, -64):
        char *= -1
        print("{}".format(chr(char) if i % 2 == 0 else chr(char + 32)), end='')
        i = i + 1


reverse_ASCII_alphabet_and_mix_case_alternatively()
