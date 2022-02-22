import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from polynomial_regressor import PolynomialRegressor
Lg = LinearRegressor()
Pr = PolynomialRegressor()



def linear(data):
    rss = 0
    ind = 0
    while ind < len(data):
        point = data[ind]
        x = point[0]
        y = point[1]
        data.remove(point)
        new_fit = Lg.fit(data, False)
        y_predicted = new_fit[0] + new_fit[1]*x
        rss += (y_predicted - y)**2
        data.insert(ind, point)
        ind += 1
    return rss


def quadratic(data):
    rss = 0
    ind = 0
    while ind < len(data):
        point = data[ind]
        x = point[0]
        y = point[1]
        data.remove(point)
        new_fit = Pr.fit(data, 2)
        y_predicted = new_fit[0] + new_fit[1]*x + new_fit[2]*x**2
        rss += (y_predicted - y)**2
        data.insert(ind, point)
        ind += 1
    return rss

def seventh_degree(data):
    rss = 0
    ind = 0
    while ind < len(data):
        point = data[ind]
        x = point[0]
        y = point[1]
        data.remove(point)
        new_fit = Pr.fit(data, 7)
        y_predicted = new_fit[0] + new_fit[1]*x + new_fit[2]*x**2 + new_fit[3]*x**3 + new_fit[4]*x**4 + new_fit[5]*x**5 + new_fit[6]*x**6 + new_fit[7]*x**7
        rss += (y_predicted - y)**2
        data.insert(ind, point)
        ind += 1
    return rss



data = [[1,3], [2,10], [3,40], [4,25], [5,90], [6,100], [7,180], [8,140], [9,250], [10,260]]
print(linear(data))
print(quadratic(data))
print(seventh_degree(data))