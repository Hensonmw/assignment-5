# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 5
Oscar Johnson 9 February 2016
"""

def appreciate():
    """
    prints "2, 4, 6, 8: Who do we appreciate?"
    """
    x = []
    for i in range(2,10,2):
        x.append(str(i)) # append to list
    y = ', '.join(x) # list to string
    y = y + ": Who do we appreciate?"
    print (y)
    
appreciate()

