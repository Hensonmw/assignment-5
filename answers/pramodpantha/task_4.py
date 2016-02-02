#!/usr/bin/env python
# utf-8

"""

calculate approximate value of e.
Created by Pramod Pantha on 31 Jan, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import math


def e_calc(u):
    e = math.fsum((1/math.factorial(n)) for n in range(u))
    return e


def main():

    u_lim1 = 1000
    u_lim2 = 10000
    e_approx1 = e_calc(u_lim1)
    e_approx2 = e_calc(u_lim2)
    print("e approximated w/ upperlimit ", u_lim1, " is ", e_approx1)
    print("e approximated w/ upperlimit ", u_lim2, " is ", e_approx2)

if __name__ == '__main__':
    main()
