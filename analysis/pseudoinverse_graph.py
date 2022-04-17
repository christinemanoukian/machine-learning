import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
import matplotlib.pyplot as plt


# data
x_coordinates = [1,2,3,4,5,6,7,8,9,10]
y_coordinates = [3,10,40,25,90,100,180,140,250,260]
data = [(1,3), (2,10), (3,40), (4,25), (5,90), (6,100), (7,180), (8,140), (9,250), (10,260)]
plt.scatter(x_coordinates, y_coordinates)

# linear
def linear(x):
    return -55.799999999999955 + 30.10909090909091*x

x_list = [num/1000 for num in range(0,20000)]
print(x_list) 
y_list = [linear(x) for x in x_list]
plt.plot(x_list, y_list, color='red')


# quadratic
def quadratic(x):
    return -10.549999999999969 + 7.484090909090668*x + 2.056818181818184*x**2

y_list = [quadratic(x) for x in x_list]
plt.plot(x_list, y_list, color='yellow')

# seventh-degree
def seventh_degree(x):
    return 993.2000785018658 - 2310.1874459590163*x + 1993.6037133768964*x**2 - 845.0513033906122*x**3 + 194.77868011207687*x**4 - 24.7766437571359*x**5 + 1.6319363768117041*x**6 - 0.04339986258890562*x**7

y_list = [seventh_degree(x) for x in x_list]
plt.plot(x_list, y_list, color='green')


plt.xlim(0,20)
plt.ylim(0,1000)
#plt.savefig('points.png')