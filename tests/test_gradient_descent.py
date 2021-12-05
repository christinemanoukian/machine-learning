import sys
sys.path.append('src')
from gradient_descent import minimize

def fprime(x):
    return 2*x
minimum = minimize(fprime, 4, 0.001, 10000)
if minimum != 0:
    print('test failed')

def fprime(x):
    return 2*x
minimum = minimize(fprime, 2, .1, 2)
if minimum != 1.28:
    print('test failed')

def fprime(x):
    return 3*x**2
minimum = minimize(fprime, 5, .001, 1000)
if minimum != .31:
    print('test failed')