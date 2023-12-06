#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    s = roman_string
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(s)):
        if i > 0 and d[s[i]] > d[s[i - 1]]:
            num += d[s[i]] - 2 * d[s[i - 1]]
        else:
            num += d[s[i]]
    return num
