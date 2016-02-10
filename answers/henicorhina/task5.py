# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 5
Oscar Johnson 9 February 2016
"""
import math 


def pi (x = math.pi):
    """
    manipulations of π
    """
    # convert to string
    one = (str(x))
    print (one, ", the type is: ", type(one))
    
    # convert to integer
    two = math.floor(x)
    print (two, ", the type is: ", type(two))
    
    # rounded to one decimal place
    three = float("{0:.1f}".format(x))
    print (three, ", the type is: ", type(three))    
    
    return x


def e_estimator(upper_limit = 5000):
    """
    estimates Euler's number to a limit of 5000
    """

    e = 2 # estimate of e  

    # some counters to keep the function running 
    n = 1
    factorial = 1
    
    for x in range(upper_limit):
        #n += 1
        #print (n)
        factorial = factorial * (n+1) 
        n += 1
        e += (1 / factorial)
        #print (e)
    return e



def main():
    e = e_estimator()
    x = pi(e)
    print (x, ", the type is: ", type(x))


if __name__ == '__main__':
    main()
