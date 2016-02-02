#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 5, Task 4
Austen T. Webber
2016_2_01
"""
# create a function that defines 'e'
import math

def e(n=10):
    return sum(1 / float(math.factorial(i)) for i in range(n))

def main_fun():
    x=20
    print(e(x))

if __name__ == '__main__':
  main_fun()
# http://stackoverflow.com/questions/23442596/calculate-e-in-python
