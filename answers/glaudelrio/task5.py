# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:39:43 2016

@author: Glaucia
"""
"""
Task 5

Copy the program you wrote for Task 3 and save it as task5.py. 
Modify the function you wrote to take π as a default argument. 
Include in this program the function you wrote to generate e. 
Call the function that produces e, and have it return a value. 
Pass that value of e to the function where you made π the default argument.

"""

#importing pi from the math module
from math import pi
import functools

def messing_with_pi(number=pi):
    """a function that modifies the value of pi to different kinds of classes or round it"""
    print("number converted to a string:")
    print(str(number))
    print("number converted to an integer:")
    print(int(number))
    print("number rounded to a single decimal place:")
    print(round(number,1))
    print("the unmodified value of number:")
    print(number)

    
    

def Calculate_e(mn=1,mx=10000):
    """calculates the euler number, and you can specify the range of numbers you will use,
    instead of going to infinity with a minimum (mn) and maximum (mx) values."""
    #setting an empty list to keep values from while loop
    values_to_sum=[]
    #setting one starting value as a denominator in the equation
    denominator= 1
    #making a while loop that runs while the "mn"value is smaller than the "mx" value.
    while (mn < mx):
        #calculating the denominators of the function one at a time
        denominator = denominator * mn
        #reseting the "mn" value, so we can get the next value in a range between the mn and
        #mx value given as arguments
        mn = mn + 1
        #appending the results of multiplication in a list as denominators of 1/
        values_to_sum.append(1/denominator)
    #summing all the values in the list made on the previous step
    eulernumber=1+(functools.reduce(lambda z, y: z+y,values_to_sum))
    #returning the calculated value
    return eulernumber



if __name__ == "__main__":
    e=Calculate_e()
    messing_with_pi(number=e)