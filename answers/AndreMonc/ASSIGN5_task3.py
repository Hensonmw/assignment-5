# !/usr/bin/env python
# encoding: utf-8

"""
My pi program
Created by Andre Moncrieff on 1 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import math

pi = math.pi


def pi_prints(x):
    """
    prints pi as different types and with different precisions
    """
    print ("string: " + str(x))
    print ("integer:",int(x))
    print ("with 1 decimal place:", round(x,1))
    print ("unmodified value:", x)
    
def main():
    pi_prints(pi)

if __name__ ==  '__main__':
    main()
    


