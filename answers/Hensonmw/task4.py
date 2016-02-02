#!/usr/bin/env python
# encoding: utf-8

"""
My 4th program for Assignment 5

Created by Michael Henson on 31 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import math

def e_number(arg1):
    X = sum(1/math.factorial(x) for x in range(arg1))
    return X
    #X = sum(1/math.factorial(x) for x in range(0,1000))
    #return X
    ##FYI range(arg1) and ragne(0,arg1) return the same answer

def main_fun():
    var1= 1000
    print(e_number(var1))

if __name__ == '__main__':
    main_fun()
