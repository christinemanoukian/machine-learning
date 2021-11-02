import sys
sys.path.append('src')
from matrix import Matrix


class LinearRegressor:
    def __init__(self):
        self.coefficients = None

    def fit(self, data):
        y = []
        for point in data:
            y_value = []
            count = len(point)-1
            if count > 0:
                y_value.append(point[count])
                count -= 1
            y.append(y_value)
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
        XtX_inverse = XtX.inverse()
        Xty = Xt.matrix_multiply(y)
        result = XtX_inverse.matrix_multiply(Xty)
        final = []
        for lst in result.elements:
            final.append(lst[0])
        final.insert(0, final.pop())
        self.coefficients = final

    def predict(self, lst):
        result = self.coefficients[0]
        count = len(lst) - 1
        while count >= 0:
            result += lst[count] * self.coefficients[count+1]
            count -= 1
        return result        
