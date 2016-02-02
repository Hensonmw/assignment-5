#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 5 Task 4

Amie Settlecowski
2 Feb. 2016

"""


import math


def e_calc(u):
    e = math.fsum((1/math.factorial(n)) for n in range(u))
    return e


def main():

    u_lim1 = 1000
    u_lim2 = 5000
    e_approx1 = e_calc(u_lim1)
    e_approx2 = e_calc(u_lim2)
    print("e approximated w/ upperlimit ", u_lim1, " is ", e_approx1)
    print("e approximated w/ upperlimit ", u_lim2, " is ", e_approx2)

if __name__ == '__main__':
    main()
