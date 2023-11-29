#!/usr/bin/python3
i = 0
for c in range(0, 26):
    print("{}".format(chr(122 - c - i)), end="")
    i = 32 if i == 0 else 0
