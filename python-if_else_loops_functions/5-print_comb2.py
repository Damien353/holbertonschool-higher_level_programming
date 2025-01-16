#!/usr/bin/python3

for i in range(0, 99):
    if i < 98:
        print("{:02}".format(i), end=", ")
    else:
        print("{:02}".format(i))
