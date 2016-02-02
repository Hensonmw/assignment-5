#!/usr/bin/env python
# #encoding: utf-8

"""
This program does four things using pi as arg1 (1) prints the value of pi and
the type of variable it is (2) changes the value of pi to a string variable and
prints both the valueand the type (3) converts pi to an integer and prints both
the value and the variable type (4) rounds pi to a single decimal plance and
prints both the value and the variable type.

Created by Alicia Reigel. 29 January 2016
Copyright Alicia Reigel. Louisiana State University. 29 January 2016. All rights
reserved.

 """
import math

def mathstuffs():
    """program first defines prints and defines pi, then it converts pi from
    a float type to a string, then it converts it to an integer and finally
    to a rounded single decimal. Each time the value and class are printed"""
    arg1= (math.pi)
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
    mathstuffs()

if __name__ == '__main__':
    main()
