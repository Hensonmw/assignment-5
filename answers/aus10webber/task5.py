#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 5, Task 5
Austen T. Webber
2016_2_01
"""

import math

# make arg1 a string, integer, round to 1 decimel place, and normal value
# For this function, arg1 = pi
def go_vols(arg1):
    print(str(arg1))
    print(int(arg1))
    print(round(arg1, 1))
    print(arg1)
    return arg1

def main_fun():
    x = e(20)
    go_vols(x)

if __name__ == '__main__':
  main_fun()

# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
# http://stackoverflow.com/questions/23442596/calculate-e-in-python
