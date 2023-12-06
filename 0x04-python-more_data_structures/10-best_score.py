#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    result = ""
    b = list(a_dictionary.values())[0]
    for i in a_dictionary:
        if a_dictionary[i] >= b:
            b = a_dictionary[i]
            result = i
    return result
