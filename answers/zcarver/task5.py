#!/usr/bin/env python
# encoding UTF-8

'''
Copy the program you wrote for Task 3 and save it as  task5.py .
Modify the function you wrote to take  π  as a default argument.
Include in this program the function you wrote to generate e. Call the function
that produces  e , and have it return a value. Pass that value of  e  to
the function where you made  π  the default argument.
'''


from math import pi
from task4_2 import euler


def print_T5(arg1=pi):
    print(str(arg1))
    print(int(arg1))
    print(round(arg1, 1))
    return(arg1)


def main():
    print_T5()
    euler5 = euler(1000)
    print_T5(euler5)

if __name__ == '__main__':
    main()
