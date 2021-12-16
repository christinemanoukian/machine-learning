import sys
sys.path.append('src')
from gradient_descent import minimize

def fx(x,y):
    return 2*x-4

def fy(x,y):
    return 2*y

minimum = minimize(fx, fy, (4,1), .001, 10000)
if minimum != 2:
    print('test failed')