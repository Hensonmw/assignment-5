#!/usr/bin/env python
# utf-8

"""

combine two strings.
Created by Pramod Pantha on 31 Jan, 2016.
Copyright 2016 Pramod Pantha. All right reserved.


"""
def combine_string():

    a = [str(n) for n in range(2, 9, 2)]
    b = 'Who do we appreciate?'
    a_str = str((','.join(a)))
    print(a_str, ':', b)

combine_string()
