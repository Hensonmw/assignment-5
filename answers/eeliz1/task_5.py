import math
##conversion of pi to string, integer, and rounded values##
def conversion(i=math.pi):
    print(i)
    print(str(i))
    print(int(i))
    print(round(i, 1))

conversion()

##calculates e##
def e(n=100):
    return sum(1/float(math.factorial(i)) for i in range(n))

##overrides default argument with e##
conversion(e())
