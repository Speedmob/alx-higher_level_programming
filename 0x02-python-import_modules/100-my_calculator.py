#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    opr = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if opr == "+":
        result = add(a, b)
    elif opr == "-":
        result = sub(a, b)
    elif opr == "*":
        result = mul(a, b)
    elif opr == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {}".format(a, opr, b, result))
