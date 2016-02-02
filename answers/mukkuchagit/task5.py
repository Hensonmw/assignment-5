#!/usr/bin/env python
# encoding: utf-8
"""
This assignment is very hard.

Created by Mukesh Maharjan on 31 Jan 2016.
Copyright 2016 Mukesh Maharjan. All rights reserved.
"""

import math
import task4


def play(arg1=math.pi):
    print(str(arg1))
    print(int(arg1))
    print(round(arg1, 1))
    print(arg1)
    return(arg1)


def main():

    play(math.pi)
    pass_e = task4.value_of_e()
    play(pass_e)


if __name__ == '__main__':
    main()
