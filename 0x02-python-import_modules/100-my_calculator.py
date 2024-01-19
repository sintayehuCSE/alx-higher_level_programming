#!/usr/bin/python3
def check_operator(operator):
    operations = ['/', '*', '-', '+']

    if len(operator) != 1:
        return False
    for i in range(len(operations)):
        if operator[0] == operations[i]:
            return True
    else:
        return False


def perform_operation(operator, oprnd1, oprnd2):
    if operator[0] == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator[0] == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator[0] == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    cmd_len = len(argv)
    if (cmd_len != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    check = check_operator(argv[2])
    if not check:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    perform_operation(argv[2], a, b)
