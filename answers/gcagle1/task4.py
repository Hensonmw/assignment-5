#! /usr/bin/env python
# encoding: utf-8
'''
Task 4

'''

import math

def approx_e(n=10):
    return sum(1 / float(math.factorial(i)) for i in range (n))



def main():
    approx_e()
    print(approx_e(10))
    
if __name__ == '__main__':
    main()

# code credit to TheifMaster and lejlot
# http://stackoverflow.com/questions/23442596/calculate-e-in-python
# accessed 02/01/2016
