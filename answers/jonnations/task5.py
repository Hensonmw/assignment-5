#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 5 Task 5
Jon Nations 30 Jan 2016
"""

from math import pi


def fact(n):
        # function source: http://stackoverflow.com/questions/20034023/
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def approximate_e():
    return 1+sum([(1)/(fact(n+1)) for n in range(3000)])

e = approximate_e()


def pi_str(pi):
    print(str(pi))


def pi_int(pi):
    print(int(pi))


def pi_round(pi):
    print("%.1f" % round(pi, 1))


def main():
    pi_str(e)
    pi_int(e)
    pi_round(e)


if __name__ == '__main__':
    main()
