#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task4
"""

import math


def task4_function(n=1000):
    return sum(1/math.factorial(x) for x in range(n))


def print_e():
    print(task4_function())


def main():
    task4_function()
    print_e()


if __name__ == '__main__':
        main()
