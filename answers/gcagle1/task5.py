#! /usr/bin/env python
# encoding: utf-8
'''
Task 5

'''
import math
import task4


def pi_ex():
    x = math.pi
    # assign pi to x
    y = (str(x))
    # convert pi to a string
    print(y)
    # print pi as a string
    z = (float(x))
    # convert pi to an integer
    print(z)
    # print pi as a string
    a = "{0:.0f}" .format(z)
    # round integer pi
    print(a)
    task4.approx_e(z)
    print(task4.approx_e(z))


def main():
    pi_ex()
    task4.approx_e()

if __name__ == '__main__':
    main()
