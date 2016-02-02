# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:22:41 2016

@author: Glaucia
"""
"""
e is a mathematical constant that is sometimes known as Euler's number 
(for the history of e, see Wikpedia. The value of e is approximately 2.71828. 
Write a program that includes a function to calculate e. Because e is computed
as the limit approaches infinity, you probably want to limit the upper range of 
values you input to the function to something (1000 < value <10,000). Once your function 
has computed e, return the approximation of e to the main loop, and print the approximate
value out.
"""

import functools
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
    e=Calculate_e(mn=1,mx=10000)
    print(e)
