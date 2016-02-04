# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:16:27 2016

@author: Marco
"""

'''
Now, we are going to play with writing a function that calls some internal 
Python functions. Start with π (which you can find in the math module - no 
need to define it). Write a function that accepts π as an argument, then 
prints each of the following: (1) π converted to a string, (2) π converted 
to an integer, and (3) π rounded to a single decimal place. Return the 
unmodified value of π and print that, as well.
'''

# importing the math module
import math

def forms_of_pi(number):
    '''function that gets any floating point number, such as "pi", and retrieves
    it in the forms of string, integer and float rounded to just one number after
    the decimal point'''
    # string    
    print(str(number))
    # integer
    print(int(number))
    # rounded
    print(round(number,1))
    # floating point
    print(number)

if __name__ == '__main__':    
    forms_of_pi(math.pi)

