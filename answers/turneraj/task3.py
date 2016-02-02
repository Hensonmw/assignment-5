#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 5

 Created by A.J. Turner on February 1, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

 """
from math import pi

def mypi(pival=pi):
    """This program sets pi as an argument and prints it as a string, an integer, and float with one decimal place"""
    print (str(pival)) #converts pi to a string
    print (int(pival))  #gives integer in pi (3)
    print (round(pival,1)) #rounds pi to have one decimal
    print (pival)

def main():
    mypi()

if __name__ == '__main__':
    main()
