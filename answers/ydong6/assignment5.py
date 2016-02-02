'''
Created on Feb 1, 2016

@author: Yuankai Dong
'''
import math
#a=math.pi

def main():
    Pi=Euler()
    print ("value PI=",Pi)

def Euler():    
    e = f = 1.0
    for i in range(2, 16):
        e += 1.0 / f
        f *= i
        #print(e)
    return e
    

if __name__ == '__main__':
    main()
   
