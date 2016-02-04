# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:31:01 2016

@author: Marco
"""

'''
So, now the tricky part. Write a program that includes a function to calculate
e. Because e is computed as the limit approaches infinity, you probably want 
to limit the upper range of values you input to the function to something 
(1000 < value <10,000). Once your function has computed e, return the 
approximation of e to the main loop, and print the approximate value out.

PS: There is a way you can compute e in a single line (and not just using
math.e, which is not the correct solution - I want you to implement the formula).
Bonus karma if you can figure out how.
'''

# I did some coorections on my tasks since I noticed by looking at the reviews
# that I forgot to define a main function for task 3, 4 and

# Importing modules
import functools
import math

def e_number():
    '''this function calculates the value of e.'''
    # empty list that later will be filled with factorial values divided by 1    
    lis=[]    
    # this next line is a for loop that calculates the factorial for each value in lis2
    [lis.append(1/(math.factorial(number))) for number in list(range(1,10000))]
    # return the correct number e by adding all values in the list 'lis'
    return 1+(functools.reduce(lambda i,j: i+j, lis))

def main():
    print (e_number())

if __name__ == '__main__':
    main()
