#!/usr/bin/env python
# utf-8

"""
Assignment 5
Task 1 Program: We appreciate `ifmain` statements!
Jessie Salter
28 January 2016
"""


def count():
    """creates a range of numbers for the count"""
    result = list(range(2, 10, 2))
    return result


def list_string():
    """converts the count list intro a string"""
    count_result = count()
    result = ", ".join([str(i) for i in count_result])
    return result


def cheer():
    """combines numbers with cheer"""
    count = list_string()
    cheer = ": Who do we appreciate?"
    print(str(count) + str(cheer))


count()
list_string()
cheer()
