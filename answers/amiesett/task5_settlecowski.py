#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 5 Task 5

Amie Settlecowski
2 Feb. 2016

"""


import math
import task4_settlecowski


def pi_print(p=math.pi, value_name="pi"):
    pi_string = str(p)
    pi_int = int(p)
    pi_rounded = round(p, 1)
    print(value_name, "as a string: ", pi_string)
    print(value_name, "as an integer ", pi_int)
    print(value_name, "to one decimal place ", pi_rounded)
    print(value_name, "as imported (a float) ", p)
    return p


def main():

    pi_print()
    approx_e = task4_settlecowski.e_calc(1000)
    pi_print(approx_e, "e")


if __name__ == '__main__':
    main()
