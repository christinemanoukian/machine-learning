import sys
sys.path.append('src')
from matrix import Matrix


class LinearRegressor:
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
        Xt = X.transpose()
        y = []
        for point in data:
            y_value = []
            y_value.append(point[1])
            y.append(y_value)
        y = Matrix(y)
        XtX = Xt.matrix_multiply(X)
        XtX_inverse = XtX.inverse()
        Xty = Xt.matrix_multiply(y)
        result = XtX_inverse.matrix_multiply(Xty)
        final = []
        final.append(result.elements[1][0])
        final.append(result.elements[0][0])
        self.coefficients = final

    def predict(self, x):
        return x * self.coefficients[1] + self.coefficients[0]
