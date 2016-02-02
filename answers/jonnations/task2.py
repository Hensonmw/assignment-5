#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 5 Task 2
Jon Nations 30 Jan 2016
"""


def cheer():
    """quick cheer no response"""
    list1 = (list(range(2, 9, 2)))
    chant = (str(list1[0]))+", "+(str(list1[1]))+", "+(str(list1[2]))+", "+(str(list1[3]))+": Who do we appreciate?"
    print(chant)


def main():
    cheer()

if __name__ == '__main__':
    main()
