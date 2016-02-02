#!/usr/bin/env python
# encoding: utf-8

"""
 My fifth task for Assignment 5. This code takes the value of Euler's number from def euler(): program and places that value in the function mypi() from the program def mypi(pival=pi):. The output is Euler's number printed as a string, an integer, and number with one decimal  place.

 Created by A.J. Turner on February 1, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

 """
from math import pi
from math import factorial

def mypi(pival=pi):
    """This program sets pi as an argument and prints it as a string, an integer, and float with one decimal place"""
    print (str(pival)) #converts pi to a string
    print (int(pival))  #gives integer in pi (3)
    print (round(pival,1)) #rounds pi to have one decimal
    print (pival)

def euler():
    """This program calculates Euler's number without using the built-in function of math.e"""
    a = list(range(0, 2000)) #setting range in list
    #print (a) #check to see if range was created in list
    new_a = list(map(lambda x: factorial(x), a))
    #print (new_a) #check to see if map and lambda are functioning in equation (ctrl + Z to quit run if taking a long time)
    next_a = list(map(lambda x: 1/x, new_a))
    #print (next_a)
    e = sum(next_a)
    return e

def main():
    e = euler()
    mypi(e)

 # call the program for Euler's number so it's run first before used in another program
 #puts Euler's number as the argument in mypi() function, so it then prints Euler's number as a string, integer, and number with one decimal place
if __name__ == '__main__':
    main()
