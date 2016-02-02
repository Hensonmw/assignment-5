# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:20:57 2016

@author: Glaucia
"""
"""
Task 1

This one is pretty simple. Write a program that calls a function that prints
 "2, 4, 6, 8: Who do we appreciate?" to the screen. Use the range() function to 
 generate the numbers. Do not (!!) use an "ifmain" statement and do not use a main() 
 function in this program - simply call the function you wrote in the body of the 
 program.
 
"""
#I will start with a function with no arguments:
def twotoeight():
    """a program that calls a function that prints "2, 4, 6, 8: Who do we appreciate?" """
    #creating the list 2, 4, 6, 8 using the functions list and range
    numbers=list(range(2,9,2))
    #printing just the numbers inside the list "numbers" plus the statement "Who do we appreciate?"
    print(str(numbers).strip('[]') + ": Who do we appreciate?")

#calling the function
twotoeight()

