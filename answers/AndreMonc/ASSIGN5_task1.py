# !/usr/bin/env python
# encoding: utf-8

"""
My appreciative program
Created by Andre Moncrieff on 1 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

def print_appr():  
    answer = list(range(2,9,2))
    stripped = str(answer).strip('[]')
    full = stripped + ": Who do we appreciate?"
    print(full)
    
print_appr()