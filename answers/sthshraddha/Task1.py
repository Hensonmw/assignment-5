#!/usr/bin/env python

"""
Task1:
This one is pretty simple. Write a program that calls a function that prints "2,
4, 6, 8: Who do we appreciate?" to the screen. Use the range() function to
generate the numbers. Do not (!!) use an "ifmain" statement and do not use a
main() function in this program - simply call the function you wrote in the
body of the program.

Created by Shraddha Shrestha on February 1, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def trial():
    lineA=(list(range(2,10,2)))
    lineB=( ", ".join((str(i) for i in lineA)))
    linec="Who do we appreciate?"
    print(lineB+":"+" "+ linec)
trial()
