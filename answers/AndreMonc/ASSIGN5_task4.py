# !/usr/bin/env python
# encoding: utf-8

"""
My e-calculating program
Created by Andre Moncrieff on 1 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

def calc_e(x=2, b=2):
    """
    This function calculates the value of e.
    Notice that x and b values change during each
    cycle through the while loop. It took me forever
    to come up with this. No one-line bonus karma :(.
    """
    eList = [2]
    while x<90000000:
        e = 1/x
        eList.append(e)
        b = b+1
        x = x * b
    else:
        e = sum(eList)
        return e

def main():
    e = calc_e()
    print(e)

if __name__ ==  '__main__':
    main()
    



