#!/usr/bin/env python
# utf-8

"""
Assignment 5
Task 4 Program: Calculating the approximate value of e
Jessie Salter
29 January 2016
"""

from math import factorial


def e_func():
    """Approximates the value of e"""
    e = sum(1 / factorial(i) for i in range(0, 5000))
    return e


def main():
    e_func()
    e = e_func()
    print(e)

if __name__ == '__main__':
    main()
