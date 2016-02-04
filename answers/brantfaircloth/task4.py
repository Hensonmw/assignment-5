#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 03 February 2016 15:53 CST (-0600)
"""

import sys
import math


def approximate_e(max_range):
    if max_range > 10000:
        print("Maximum of range is too high")
        sys.exit()
    else:
        return sum([1 / math.factorial(i) for i in range(0, max_range)])


def main():
    print(approximate_e(1000))

if __name__ == '__main__':
    main()
