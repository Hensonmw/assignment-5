# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 5
Oscar Johnson 9 February 2016
"""

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


def main():
    x = pi()
    print (x, ", the type is: ", type(x))


if __name__ == '__main__':
    main()
