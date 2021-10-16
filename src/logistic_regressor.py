import sys
sys.path.append('src')
from matrix import Matrix
from numpy import log as ln
from math import exp as e


class LogisticRegressor:
    def __init__(self):
        self.coefficients = None

    def fit(self, data):
        X = []
        for point in data:
            x = []
            x.append(point[0])
            x.append(1)
            X.append(x)
        X = Matrix(X)
        y = []
        for point in data:
            value = []
            value.append(ln((1 / point[1]) - 1))
            y.append(value)
        y = Matrix(y)
        Xt = X.transpose()
        XtX = Xt.matrix_multiply(X)
        Xty = Xt.matrix_multiply(y)
        XtX_inverse = XtX.inverse()
        result = XtX_inverse.matrix_multiply(Xty)
        final = []
        final.append(result.elements[0][0])
        final.append(result.elements[1][0])
        self.coefficients = final

    def predict(self, x):
        e_exponent = self.coefficients[0] * x + self.coefficients[1]
        e_value = e(e_exponent)
        denominator = 1 + e_value
        answer = 1 / denominator
        return answer
