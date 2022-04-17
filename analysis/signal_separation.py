import sys
sys.path.append('src')
from matrix import Matrix
import math
import matplotlib.pyplot as plt



def fit(data):

    y = [[point[1]] for point in data]
    y = Matrix(y)

    X = []
    for point in data:

        X_point = []
        X_point.append(math.sin(point[0]))
        X_point.append(math.cos(point[0]))
        X_point.append(math.sin(2*point[0]))
        X_point.append(math.cos(2*point[0]))
        X.append(X_point)

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

    return final

def plot(x):
    return 0.9987714718466099*math.sin(x) + 2.000855468831855*math.cos(x) - 3.0006300919504056*math.sin(2*x) + 5.000550805490717*math.cos(2*x)


data = [(0.0, 7.0), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
 (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
 (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22),
 (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
 (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]


x_list = [num/10 for num in range(0,50)]

y_list = [plot(x) for x in x_list]



x_coordinates = []
y_coordinates = []
for point in data:
    x_coordinates.append(point[0])
    y_coordinates.append(point[1])

plt.scatter(x_coordinates, y_coordinates)
plt.plot(x_list, y_list)
plt.savefig('signal_separation.png')