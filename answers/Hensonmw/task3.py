#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 5

Created by Michael Henson on 31 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""

import math

def math_fun(arg1):
    print(str(arg1))
    print(int(arg1))
    print(round(arg1, 1))
    print(arg1)
    return arg1

def main_fun():
    var1 = math.pi
    math_fun(var1)

if __name__ == '__main__':
    main_fun()
