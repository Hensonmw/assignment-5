'''
Created on Feb 1, 2016

@author: Yuankai Dong
'''

import math
a=math.pi

def main():
    print (a)
def main1():
    b=round (a,1)
    print(b)
def main2():
    print ("a")
    c="3.14"
    d=str(a)
    print (d)
    print(type(d))
def main3():
    e=int(a)
    print(e)
    print (type(e))

if __name__ == '__main__':
   main()
   main1()
   main2()
   main3()