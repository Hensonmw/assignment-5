#!/usr/bin/env python
# encoding: utf-8
"""
This assignment was very hard.

Created by Mukesh Maharjan on 31 Jan 2016.
Copyright 2016 Mukesh Maharjan. All rights reserved.
"""

import math


def value_of_e():
    e = sum(1 / math.factorial(i) for i in range(1001))
    return e


def main():
    print(value_of_e())

if __name__ == '__main__':
    main()
