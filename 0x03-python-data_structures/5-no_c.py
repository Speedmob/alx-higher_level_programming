#!/usr/bin/python3
def no_c(my_string):
    s = {ord('c'): None, ord('C'): None}
    return my_string.translate(s)
