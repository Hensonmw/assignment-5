#!/usr/bin/env python
# encoding UTF-8

'''
task3-call internal python fxns. Start with π (which is found in 'math')
Write a fxn that accepts π as an argument, then prints each of the following:
(1)  π  converted to a string,
(2)  π  converted to an integer, and
(3)  π  rounded to a single decimal place. Return the unmodified value of  π.
'''
import math

arg1 = math.pi


def print_T3():
    print(str(arg1))
    print(int(arg1))
    print(round(arg1, 1))

print_T3()
