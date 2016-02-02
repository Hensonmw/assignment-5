# !/usr/bin/env python
# encoding: utf-8

"""
My import program
Created by Andre Moncrieff on 1 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

Notice that at the beginning of the output I get an extra 
"2, 4, 6, 8: Who do we appreciate?" 

I get this unwanted repetition because when I import ASSIGN5_task1 it is
automatically run (I don't have the "ifmain" statement in that file).
"""

import ASSIGN5_task1 


def class_chant():
    ASSIGN5_task1.print_appr()
    print("Our teacher! Our teacher!")
    ASSIGN5_task1.print_appr()
    print("Our teacher! Our teacher!")

class_chant()

