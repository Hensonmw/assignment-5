# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:11:02 2016

@author: Glaucia
"""
"""
Task 3

Now, we are going to play with writing a function that calls some internal Python 
functions. Start with π (which you can find in the math module - no need to define it). 
Write a function that accepts π as an argument, then prints each of the following: 
(1) π converted to a string, (2) π converted to an integer, and (3) π rounded to a 
single decimal place. Return the unmodified value of π and print that, as well.

"""
#importing pi from the math module
from math import pi


def messing_with_pi(arg):
    """a function that modifies the value of pi to different kinds of classes or round it"""
    print("pi converted to a string:")
    print(str(arg))
    print("pi converted to an integer:")
    print(int(arg))
    print("pi rounded to a single decimal place:")
    print(round(arg,1))
    print("the unmodified value of pi:")
    print(arg)

    

if __name__ == "__main__":
    messing_with_pi(arg=pi)