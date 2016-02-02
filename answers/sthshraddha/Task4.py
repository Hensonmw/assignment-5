#!/usr/bin/env python

"""
Task 4:

e is a mathematical constant that is sometimes known as Euler's number
(for the history of e, see Wikpedia). The value of e is approximately 2.71828.
The reason that e is an approximate value is because it is computed as:
e formula:
So, now the tricky part. Write a program that includes a function to calculate
e. Because e is computed as the limit approaches infinity, you probably want to
limit the upper range of values you input to the function to something
(1000 < value <10,000). Once your function has computed e, return the apprx
of e to the main loop, and print the approximate value out.
PS: There is a way you can compute e in a single line (and not just using
math.e, which is not the correct solution - I want you to implement the
formula). Bonus karma if you can figure out how.

Credit url: http://www.codecodex.com/wiki/Calculate_digits_of_e
Date accessed: Feb 2nd, 2016

Created by Shraddha Shrestha on February 2, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


from math import factorial


def euler_calculation():
    euler_calculation=sum(1/(factorial(i)) for i in range(0, 9000))
    return euler_calculation


def main():
    euler=euler_calculation()
    print (euler)

if __name__ == '__main__':
    main()
