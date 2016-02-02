#!/usr/bin/env python

"""
Task2:
Write a second program that uses the program you wrote for Task 1 to
demonstrate why I have suggested that you should always use a main() function
along with the "ifmain" statement. Do not alter your first program.
Note to self: To print multiple lines we need to have print(""" """)

Created by Shraddha Shrestha on February 1, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


from Task1 import trial


def reason():
    print("""script can be used to run the entire function at once as well as
part of the script can be used to run a calculation. Without "ifmain"statement,
the entire script will run without defining a specific function. For instace,
here we are importing script for task 1 and it will still run here. But, if we
were to select "trial" function in a different script, it would not be possible
without "ifmain" statement.""")


def main():
        reason()

if __name__ == '__main__':
    main()
