# !/usr/bin/env python
# encoding: utf-8

"""
My combo program
Created by Andre Moncrieff on 1 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import math

pi = math.pi

def pi_prints(x=pi):
    """
    prints pi as different types and with different precisions
    """
    print ("string: " + str(x))
    print ("integer:",int(x))
    print ("with 1 decimal place:", round(x,1))
    print ("unmodified value:", x)
    
def calc_e(x=2, b=2):
    """
    This function calculates the value of e.
    Notice that x and b values change during each
    cycle through the while loop. It took me forever
    to come up with this. No one-line bonus karma :(.
    """
    eList = [2]
    while x<90000000:
        fraction = 1/x
        eList.append(fraction)
        b = b+1
        x = x * b
    else:
        e = sum(eList)
        return e


def main():
    e = calc_e()
    pi_prints(e)

if __name__ ==  '__main__':
    main()

