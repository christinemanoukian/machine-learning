import sys
sys.path.append('src')
from matrix import Matrix

from numpy import log as ln


def linear_regression(points):
    X = []
    for point in points:
        x = []
        x.append(point[0])
        x.append(1)
        X.append(x)
    X = Matrix(X)
    Xt = X.transpose()
    y = []
    for point in points:
        y_value = []
        y_value.append(point[1])
        y.append(y_value)
    y = Matrix(y)
    XtX = Xt.matrix_multiply(X)
    XtX_inverse = XtX.inverse()
    Xty = Xt.matrix_multiply(y)
    result = XtX_inverse.matrix_multiply(Xty)
    return result


def logistic_regression(points):
    X = []
    for point in points:
        x = []
        x.append(point[0])
        x.append(1)
        X.append(x)
    X = Matrix(X)
    y = []
    for point in points:
        value = []
        value.append(ln((1 / point[1]) - 1))
        y.append(value)
    y = Matrix(y)
    Xt = X.transpose()
    XtX = Xt.matrix_multiply(X)
    Xty = Xt.matrix_multiply(y)
    XtX_inverse = XtX.inverse()
    result = XtX_inverse.matrix_multiply(Xty)
    return result


linear_regression([[1,.2], [2,.25], [3,.5]]).print()
logistic_regression([[1,.2], [2,.25], [3,.5]]).print()