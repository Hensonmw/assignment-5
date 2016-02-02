#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 5 Task 4
Jon Nations. 30 January 2016
"""


def fact(n):
        # function source: http://stackoverflow.com/questions/20034023/
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def approximate_e():
    return 1+sum([(1)/(fact(n+1)) for n in range(3000)])


def main():
    print(approximate_e())

if __name__ == '__main__':
        main()
