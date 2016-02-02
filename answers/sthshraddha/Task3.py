#!/usr/bin/env python

"""
Task 3:

Now, we are going to play with writing a function that calls some internal
Python functions. Start with π (which you can find in the math module - no need
to define it). Write a function that accepts π as an argument, then prints
each of the following: (1) π converted to a string, (2) π converted to an
integer, and (3) π rounded to a single decimal place. Return the unmodified
value of π and print that, as well.

Created by Shraddha Shrestha on February 1, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def math_pi():
    import math
    print("pi as string: " + str(math.pi))
    print("pi as integer: " + str(int(math.pi)))
    print("pi as rounded value to one decimal value: " + str(round(math.pi,1)))
    print("pi as unmodified value: " + str(math.pi))


def main():
    math_pi()

if __name__ == '__main__':
    main()
