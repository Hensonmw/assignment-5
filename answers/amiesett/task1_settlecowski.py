#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 5 Task 1

Amie Settlecowski
2 Feb. 2016

"""


def cheer():

    count = [str(n) for n in range(2, 9, 2)]
    phrase = 'Who do we appreciate?'
    count_str = str((','.join(count)))
    print(count_str, ':', phrase)

cheer()
