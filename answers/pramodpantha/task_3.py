#!/usr/bin/env python
# utf-8

"""

Created by Pramod Pantha on 31 Jan, 2016.
Copyright 2016 Pramod Pantha. All right reserved.


"""


import math


def pi_print(p):
    pi_string = str(p)
    pi_int = int(p)
    pi_rounded = round(p, 1)
    print("pi as a string: ", pi_string)
    print("pi as an integer ", pi_int)
    print("pi as a decimal ", pi_rounded)
    print("pi as imported from math (a float) ", p)
    return p


def main():

    pi = math.pi
#    print("math.py type is ", type(pi))
    pi_again = pi_print(pi)

if __name__ == '__main__':
    main()
