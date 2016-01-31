#!/usr/bin/env python
# #encoding: utf-8

"""
Program to print "2,4,6,8. Who do we appreciate?" AND demonstrate why an
"if main statement" is ideal when writing programs.

Created by Alicia Reigel. 29 January 2016.
Copyright Alicia Reigel. Louisiana State University. 29 January 2016.

"""
from reigeltask1_5 import appreciate_function

def main():
    #prints a statement explaining why an if main statement is ideal in program creation.
    print("There is no main function in the python program where appreciate_function was created and therefore when it is imported into this program and this program is run the appreciate_function runs automatically, as you see here, If there had been a main function that program would not have run automatically.")

if __name__ == '__main__':
        main()
