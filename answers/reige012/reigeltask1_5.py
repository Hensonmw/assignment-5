#!/usr/bin/env python
# #encoding: utf-8

"""
Program to print "2,4,6,8. Who do we appreciate?"

Created by Alicia Reigel. 29 January 2016.
Copyright Alicia Reigel. Louisiana State University. 29 January 2016.

"""

def appreciate_function():
    """Prints a range of numbers separated by 2, followed by a silly statement"""
    print(*range(2,9,2),sep=',', end="")
    print(": Who do we appreciate?")

appreciate_function()
