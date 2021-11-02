import sys
sys.path.append('src')
from matrix import Matrix
from math import log as ln
from math import exp as e


class LogisticRegressor:
    def __init__(self):
        self.coefficients = None

    def fit(self, data):
        y = []
        for point in data:
            value = []
            count = len(point) - 1
            if count > 0:
                value.append(ln((1 / point[count]) - 1))
                count -= 1
            y.append(value)
        y = Matrix(y)
        X = []
        for point in data:
            x = []
            count = 0
            while count < len(point) - 1:
                x.append(point[count])
                count += 1
            x.append(1)
            X.append(x)
        X = Matrix(X)
        Xt = X.transpose()
        XtX = Xt.matrix_multiply(X)
        Xty = Xt.matrix_multiply(y)
        XtX_inverse = XtX.inverse()
        result = XtX_inverse.matrix_multiply(Xty)
        final = []
        for lst in result.elements:
            final.append(lst[0])
        self.coefficients = final

    def predict(self, lst):
        length = len(self.coefficients) - 1
        e_exponent = self.coefficients[length]
        count = 0
        while count < length:
            e_exponent += self.coefficients[count] * lst[count]
            count += 1
        e_value = e(e_exponent)
        denominator = 1 + e_value
        result = 1 / denominator
        return result
