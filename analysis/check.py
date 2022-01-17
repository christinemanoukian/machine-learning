from math import exp as e

def function(a, b):
    return -1 - .01 * (2*(1/(1+e(a+b))-.5) * (-e(a+b))/((1+e(a+b))**2) + 2*(1/(1+e(4*a+b))-1) * (-4*e(4*a+b))/((1+e(4*a+b))**2))

print(function(-1,0))