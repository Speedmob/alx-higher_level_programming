#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    args = "arguments:"
    if argc == 2:
        args = "argument:"
    if argc == 1:
        args = "arguments."
    print("{:d} {}".format((argc - 1), args))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
