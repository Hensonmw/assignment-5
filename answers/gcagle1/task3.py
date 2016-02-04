#! /usr/bin/env python
# encoding: utf-8
'''
Task 3

'''
import math


def pi_ex():
    x = math.pi
    # assign pi to x
    y = (str(x))
    # convert pi to a string
    print(y)
    # print pi as a string
    z = (int(x))
    # convert pi to an integer
    print(z)
    # print pi as a string
    a = "{0:.0f}" .format(z)
    # round integer pi
    print(a)


def main():
    pi_ex()

if __name__ == '__main__':
    main()
