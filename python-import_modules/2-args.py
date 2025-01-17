#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = len(sys.argv)
    arguments_count = arguments - 1  # argu passes sans compter nom script
    if arguments_count == 0:
        print("0 arguments.")
    elif arguments_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments_count))
    for i in range(1, arguments):
        print("{}: {}".format(i, sys.argv[i]))
