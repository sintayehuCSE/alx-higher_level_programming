#!/usr/bin/python3
def subtract(list_sum):
    sub = 0
    max_sum = max(list_sum)
    for i in list_sum:
        if max_sum > i:
            sub += i
    return max_sum - sub


def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    elif not isinstance(roman_string, str):
        return (0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key = list(roman.keys())
    sum = 0
    last_rom = 0
    list_sum = [0]
    for char in roman_string:
        for rom_num in key:
            if rom_num == char:
                if roman[char] <= last_rom:
                    sum += subtract(list_sum)
                    list_sum = [roman[char]]
                else:
                    list_sum.append(roman[char])
                last_rom = roman[char]
    sum += subtract(list_sum)
    return sum
