#!/usr/bin/env python
# utf-8

"""
Assignment 5
Task 3 Program: Getting Math-y
Jessie Salter
29 January 2016
"""

from math import pi


def pi_func(arg1):
    """Converts floating point to string, integer, and rounds to nearest tenth.
    Prints the value and its type."""
    print(str(arg1), type(str(arg1)))
    print(int(arg1), type(int(arg1)))
    print(round(arg1, 1), type(round(arg1, 1)))


def main():
    arg1 = pi
    print(str("input ="), arg1, type(arg1))
    pi_func(arg1)


if __name__ == '__main__':
    main()
