import sys
sys.path.append('src')
from matrix import Matrix


class PolynomialRegressor:
    def __init__(self):
        self.coefficients = None

    def fit(self, data, n):
        y = []
        coordinate = len(data[0])-1
        for point in data:
            y_value = []
            y_value.append(point[coordinate])
            y.append(y_value)
        y = Matrix(y)
        X = []
        for point in data:
            x = []
            count = 0
            n_count = 2
            x.append(1)                
            while count < len(point) - 1:
                x.append(point[count])
                while n_count <= n:
                    x.append(point[count]**n_count)
                    n_count += 1                
                count += 1
            X.append(x) 
        X = Matrix(X)
        Xt = X.transpose()
        XtX = Xt.matrix_multiply(X)
        XtX_inverse = XtX.inverse()
        result = XtX_inverse.matrix_multiply(Xt)
        result = result.matrix_multiply(y)
        result = result.elements
        final = []
        for element in result:
            final.append(element[0])
        self.coefficients = final
        return final


data = [(-1,2),(1,0),(2,4)]
Pr = PolynomialRegressor()
Pr.fit(data, 3)
print(Pr.coefficients)