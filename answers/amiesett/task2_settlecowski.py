#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 5 Task 2

Amie Settlecowski
2 Feb. 2016

** Demonstrates why you should always use the "ifmain" statement: When this
program imports task1_settlecowski, because I didn't use the "ifmain" statement
in that script, the whole task1 program runs. This explains why "2,4,6,8: Who
do we appreciate" prints to screen 2x even though I only call it once here.**
"""


import task1_settlecowski

task1_settlecowski.cheer()
