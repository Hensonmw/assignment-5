# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Sun Jan 31 21:35:26 2016
@author: Marco
"""

'''This one is pretty simple. Write a program that calls a function that prints 
"2, 4, 6, 8: Who do we appreciate?" to the screen. Use the range() function to 
generate the numbers. Do not (!!) use an "ifmain" statement and do not use a 
main() function in this program - simply call the function you wrote in the 
body of the program.'''

def numbers(first, last, step=1):
    """creates a range of numbers. The arguments are the same as in the range funciton.
    This function will also print the phrase 'Who do we appreciate' at the end"""
    list_of_numbers =  list(range(first, last, step))
    number_string = str([number for number in list_of_numbers])
    print (str(number_string[1:-1]) + ': Who do we appreciate?')


numbers(2, 9, 2)