#!/usr/bin/env python
# utf-8

"""
Assignment 5
Task 2 Program: Why do we appreciate `ifmain` statements?
Jessie Salter
29 January 2016
"""

import jsalt_task1


def explanation():
    print('''
    Because jsalt_task1 does not have an `ifmain` statement, when I import it
    to this program it automatically runs with this program (hence the cheer
    printed above).''')


def main():
    explanation()

if __name__ == '__main__':
    main()
