#!/usr/bin/env python
# encoding UTF-8

'''
Task4-write a prog that includes a fxn to calculate e. Return the approximation
to the main loop and print the value.
'''

import math


def euler(r):
    e = sum(1/math.factorial(i) for i in range(r))
    return e


def main():
    r = 1000
    euler(r)
    e = euler(r)
    print(e)

if __name__ == '__main__':
    main()
