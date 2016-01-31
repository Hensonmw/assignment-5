#!/usr/bin/env python
# encoding: utf-8

"""
My first program for Assignment 5

Created by Michael Henson on 31 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""

## in str ii used [] which is slice. This allows you to slice the first int to
## the last
def cheer():
    number = list(range(2,9,2))
    number2 = str(number)[1:-1]
    saying = " Who do we appreciate!"
    print(number2, saying, sep=':')
cheer()
