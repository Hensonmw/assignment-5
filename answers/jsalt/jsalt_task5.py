#!/usr/bin/env python
# utf-8

"""
Assignment 5a
Task 5 Program: Getting Math-y with e
Jessie Salter
29 January 2016
"""

from math import pi
from jsalt_task4 import e_func


def pi_func(arg2, arg1=pi):
    """Converts floating point to string, integer, and rounds to nearest tenth.
    Prints the value and its type."""
    print(str(arg1), type(str(arg1)))
    print(int(arg1), type(int(arg1)))
    print(round(arg1, 1), type(round(arg1, 1)))
    print(str(arg2), type(str(arg2)))
    print(int(arg2), type(int(arg2)))
    print(round(arg2, 1), type(round(arg2, 1)))


def main():
    arg1 = pi
    arg2 = e_func()
    print(str("default input ="), arg1, type(arg1))
    print(str("input ="), arg2, type(arg2))
    pi_func(arg2)

if __name__ == '__main__':
    main()
