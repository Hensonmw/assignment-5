#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 5

 Created by A.J. Turner on February 1, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

 """

def mytask1():
     """function concatenates two strings and prints them as one, but without the 'main'function and 'ifmain'statement as instructed"""
     list1 = list(range(2,9,2))
     #print (list1) #check to see if list command worked
     abc = str(list1[0])+", "+ str(list1[1])+", "+str(list1[2])+", "+str(list1[3])+ ": Who do we appreciate?"   #string function concatenates list1 with text (combining diff types)

     print (abc)

mytask1()
