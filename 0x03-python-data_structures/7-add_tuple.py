#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_tup = tuple_a + (0, 0)
    second_tup = tuple_b + (0, 0)
    return (first_tup[0] + second_tup[0], first_tup[1] + second_tup[1])
