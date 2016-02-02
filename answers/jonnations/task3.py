#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 5 Task 3
Jon Nations 30 Jan 2016
"""

from math import pi


def pi_str(pi):
    print(str(pi))


def pi_int(pi):
    print(int(pi))


def pi_round(pi):
    print("%.1f" % round(pi, 1))


def main():
    pi_str(pi)
    pi_int(pi)
    pi_round(pi)


if __name__ == '__main__':
    main()
