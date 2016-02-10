# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:59:09 2016

@author: Marco
"""

'''Task 5'''

'''Copy the program you wrote for Task 3 and save it as task5.py. Modify the 
function you wrote to take π as a default argument. Include in this program 
the function you wrote to generate e. Call the function that produces e, and 
have it return a value. Pass that value of e to the function where you made π 
the default argument.'''

# I did some coorections on my tasks since I noticed by looking at the reviews
# that I forgot to define a main function for task 3, 4 and

import math
import task4


def forms_of_pi(number=math.pi):
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

def main():
    number = task4.e_number()
    forms_of_pi(number)
    
if __name__ == '__main__':
    main()
    
    
    