#!/usr/bin/env python
# encoding: utf-8

"""
 My fourth task for Assignment 5

 Created by A.J. Turner on February 1, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

 """
from math import factorial

def euler():
    """This program calculates Euler's number without using the built-in function of math.e"""
    a = list(range(0, 2000)) #setting range in list
    #print (a) #check to see if range was created in list
    new_a = list(map(lambda x: factorial(x), a))
    #print (new_a) #check to see if map and lambda are functioning in equation (ctrl + Z to quit run)
    next_a = list(map(lambda x: 1/x, new_a))
    #print (next_a)
    e = sum(next_a)
    return e

def main():
    e = euler()
    print(e)

if __name__ == '__main__':
    main()





    #facts = factorial(new_a)  #finding factorial of numbers in range
    #facts2 = 1/facts  #dividing 1 by factorial of range
