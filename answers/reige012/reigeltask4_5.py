#!/usr/bin/env python
# #encoding: utf-8

"""
This program approximates the mathematical value of e when n= 0-1500.

Created by Alicia Reigel. 31 January 2016
Copyright Alicia Reigel. Louisiana State University. 31 January 2016. All rights
reserved.

 """

from math import factorial

def alicia_factorial():
    """approximates the value of e"""
    aliciase=sum(1/(factorial(i)) for i in range(0, 1500))
    return aliciase

def main():
    alicia_factorial()
    e=alicia_factorial()
    print(e)

if __name__ == '__main__':
    main()
