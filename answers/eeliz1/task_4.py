import math

##defines and prints the function e, which will calculate the constant e to n = 100##
def e(n=100):
    return sum(1/float(math.factorial(i)) for i in range(n))

print(e())
