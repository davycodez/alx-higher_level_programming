#!/usr/bin/python3
for i in range(100):
    if i > 98:
        print("{0:0=2d}".format(i))
    else:
        print("{0:0=2d}".format(i), end=', ')
