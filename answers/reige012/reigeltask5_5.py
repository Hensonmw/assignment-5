#!/usr/bin/env python
# #encoding: utf-8

"""
This program alters the mathstuffs program previously created by me to make the
pi a default argument if no alternate value is defined and then defines e from my
aliciase program as the alternate value. Cool stuff.

Created by Alicia Reigel. 31 January 2016
Copyright Alicia Reigel. Louisiana State University. 31 January 2016. All rights
reserved.

 """
from math import pi
from reigeltask4_5 import alicia_factorial

def new_pi_e(arg1=pi):
    """program prints and defines pi, converts pi from a float type to a string,
    then to an integer and finally to a rounded single decimal. Each time the value
    and class are printed"""
    print(arg1)
    print(type(arg1))
    arg2=str(arg1)
    print(arg2)
    print(type(arg2))
    arg3=int(arg1)
    print(arg3)
    print(type(arg3))
    arg4=round(arg1, 1)
    print(arg4)
    print(type(arg4))

def main():
    alicia_factorial()
    e=alicia_factorial()
    new_pi_e(e)

if __name__ == '__main__':
    main()
