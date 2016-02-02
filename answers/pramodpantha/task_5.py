#!/usr/bin/env python
# utf-8

"""
BIOL7800 Task 5 of Assignment 5
Created by Pramod Pantha on 31 Jan, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import math
import task_4


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
    approx_e = task_4.e_calc(1000)
    pi_print(approx_e, "e")


if __name__ == '__main__':
    main()
