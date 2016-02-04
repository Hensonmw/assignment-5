'''
Created on Feb 1, 2016

@author: Yuankai Dong
'''
def main():
    from decimal import Decimal, getcontext
    getcontext().prec = 1000 # set the precision to 1000 places
    e = Decimal(0)
    f = Decimal(1)
    n = Decimal(1)
    while True:
        olde = e
        e += Decimal(1) / f
        if e == olde: # if there was no change in the 1000 places, stop.
            break
        f *= n
        n += Decimal(1)
    print(float(e))


if __name__ == '__main__':
   main()
   