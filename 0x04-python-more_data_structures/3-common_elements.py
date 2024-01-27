#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for first in set_1:
        for second in set_2:
            if first == second:
                new_set.add(first)
    return new_set
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
