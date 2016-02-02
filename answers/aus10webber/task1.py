#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 5, Task 1
Austen T. Webber
2016_2_01
"""

# Define function to print a range of numbers and a phrase
def cheer():
    number = list(range(2,9,2))
    number2 = str(number)[1:-1]
    saying = " Who do we appreciate!"
    print(number2, saying, sep=':')
cheer()

#http://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python
