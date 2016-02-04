#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 03 February 2016 15:50 CST (-0600)
"""

import math


def display_pi(pi):
    print("pi as a string:", str(pi))
    print("pi as an int:", int(pi))
    print("pi rounded:", round(pi, 1))
    return pi


def main():
    pi = display_pi(math.pi)
    print("The returned value of pi is: ", pi)


if __name__ == '__main__':
    main()
