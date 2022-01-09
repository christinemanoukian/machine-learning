import sys
sys.path.append('src')
from matrix import Matrix
from math import log as ln
from math import exp as e


class LogisticRegressor:
    def __init__(self, m, M):
        self.coefficients = None
        self.m = m
        self.M = M

    def fit(self, data, interaction_terms):
        y = []
        for point in data:
            value = []
            count = len(point) - 1
            if count > 0:
                value.append(ln((self.M - point[count]) / (point[count] - self.m)))
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
            if interaction_terms == True:
                count1 = 0
                count2 = 1
                while count1 <= len(point) - 3 and count2 <= len(point) - 1:
                    if count2 == len(point) - 1:
                        count2 = 1
                        count1 += 1
                    if count1 >= count2:
                        count2 += 1
                    else:
                        x.append(point[count1] * point[count2])
                        count2 += 1
            x.append(1)                
            X.append(x) 
        X = [[round(num, 1) for num in lst] for lst in X]
        X = Matrix(X)
        Xt = X.transpose()
        XtX = Xt.matrix_multiply(X)
        XtX = [[round(num, 2) for num in lst] for lst in XtX.elements]
        XtX = Matrix(XtX)
        Xty = Xt.matrix_multiply(y)
        XtX_inverse = XtX.inverse()
        result = XtX_inverse.matrix_multiply(Xty)
        final = []
        for lst in result.elements:
            final.append(lst[0])
        final = [round(num, 2) for num in final]
        self.coefficients = final

    def predict(self, lst):
        length = len(self.coefficients) - 1
        e_exponent = self.coefficients[length]
        count1 = 0
        count2 = 0
        while count2 < len(lst):
            e_exponent += self.coefficients[count1] * lst[count2]
            count1 += 1
            count2 += 1
        if interaction_terms == True:
            count1 = 0
            count2 = 1
            while count1 <= len(lst) - 3 and count2 <= len(lst) - 1:
                if count2 == len(lst) - 1:
                    count2 = 1
                    count1 += 1
                if count1 >= count2:
                    count2 += 1
                else:
                    e_exponent += lst[count1] * lst[count2]
                    count2 += 1            
        e_value = e(e_exponent)
        denominator = 1 + e_value
        numerator = self.M - self.m
        result = self.m + numerator / denominator
        result = round(result, 1)
        return result

reg = LogisticRegressor(.1, 10)
data = [[2,.9], [3,.95], [4,1]]
interaction_terms = False
reg.fit(data, interaction_terms)
print(reg.coefficients)