#!/usr/bin/python3
def print_last_digit(number):
    r = number % 10
    if number < 0:
        r = (-1 * number) % 10
    print(r, end="")
    return r
