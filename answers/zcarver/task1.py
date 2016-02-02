#! /usr/bin/env python
# encoding UTF-8
'''
Task1-write a prog that calls a fxn that prints"2,4,6,8:Who do we appreciate?"
Use the rang() fxn to generate the numbers. Do not use an 'ifmain' statement&
do not use a main() fxn in this prog-simply call the fxn you wrote in the body.
'''


def print_T1():
    print(list(range(2, 10, 2)), ('who do we appreciate?'))
print_T1()
