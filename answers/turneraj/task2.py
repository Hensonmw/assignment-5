#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 5

 Created by A.J. Turner on February 1, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

 """
"""#importing program from task 1 will simply run everything in the program because
the 'main() function and 'ifmain' statement were not used. Using the 'main()'
function and 'ifmain' statement allows you to only execute what parts
(functions) you want to run within a reusable module."""
import task1

def mytask2():
    task1.mytask1() #calls function created in task1 to run once, but it gives
    #two outputs of the answer because 'main()' and "ifmain" were not used in
    # the original program

mytask2()
