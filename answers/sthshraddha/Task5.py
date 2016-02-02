#!/usr/bin/env python

"""
Task 5:

Copy the program you wrote for Task 3 and save it as task5.py. Modify the
function you wrote to take π as a default argument. Include in this program the
function you wrote to generate e. Call the function that produces e, and have
it return a value. Pass that value of e to the function where you made π the
default argument.

Note to self: Here I am importing euler_calcuation function from Task4. I am
defining a new function to do same thing as Task3 as new_math_pi_replace_by_e.
The default argument (arg1) is math.pi. The script is same as Task3.
Then I am defining a "main" function where I am calling euler_calcuation,
giving arg2 value from euler_calcuation function. Then I pass this value to
new_math_pi_replace_by_e function, finally replacing default argument by arg2.

Created by Shraddha Shrestha on February 2, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


import math
from Task4 import euler_calculation


def new_math_pi_replace_by_e(arg1=math.pi):
    print("pi as string: " + str(arg1))
    print("pi as integer: " + str(int(arg1)))
    print("pi as rounded value to one decimal value: " + str(round(arg1,1)))
    print("pi as unmodified value: " + str(arg1))


def main():
    euler_calculation()
    arg2=euler_calculation()
    new_math_pi_replace_by_e(arg2)


if __name__ == '__main__':
    main()
