import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

reg = LinearRegressor()
data = [[1,3], [0,1], [2,2]]
reg.fit(data)
if reg.coefficients != [1.5, 0.5000000000000004]:
    print('reg.coefficients failed on input [(1,3), (0,1), (2,2)]')
if reg.predict([4]) != 3.5000000000000018:
    print('reg.predict failed on input 4')
data2 = [[1,.2], [2,.25], [3,.5]]
reg.fit(data2)
if reg.coefficients != [0.016666666666666607, 0.15000000000000002]:
    print('reg.coefficients failed on input [(1,.2), (2,.25), (3,.5)]')
if reg.predict([4]) != 0.6166666666666667:
    print('reg.predict failed on input 4')
if reg.predict([1]) != 0.16666666666666663:
    print('reg.predict failed on input 1')
data5 = [[0,0,1], [1,0,2], [2,0,4], [4,0,8], [6,0,9], [0,2,2], [0,4,5], [0,6,7], [0,8,6]]
reg.fit(data5)
if reg.predict([5,0]) != 8.259740259740258:
    print('reg.predict failed on input [5,0]')
if reg.predict([5,5]) != 12.051948051948047:
    print('reg.predict failed on input [5,5]')

reg2 = LogisticRegressor()
data3 = [[1,.2], [2,.25], [3,.5]]
reg2.fit(data3)
if reg2.coefficients != [-0.6931471805599452, 2.21459657771589]:
    print('reg.coefficients failed on input [(1,.2), (2,.25), (3,.5)]')
if reg2.predict([4]) != 0.6359878341047968:
    print('reg.predict failed on input 4')
    print(reg2.predict([4]))
data4 = [[1,.3], [1,.4], [2,.3]]
reg2.fit(data4)
if reg2.coefficients != [0.2209163761395203, 0.4054651081081637]:
    print('reg.coefficients failed on input [(1,.3), (1,.4), (2,.3)]')
if reg2.predict([4]) != 0.21599999999999966:
    print('reg.predict failed on input 4')
if reg2.predict([1]) != 0.3483314773547883:
    print('reg.predict failed on input 1')
data6 = [[0,0,.2], [2,0,.2], [2,0,.4], [4,0,.8], [6,0,.9], [0,2,.2], [0,4,.5], [0,6,.7], [0,8,.6]]
reg2.fit(data6)
if reg2.predict([5,0]) != 0.8253318675847905:
    print('reg.predict failed on input [5,0]')
if reg2.predict([5,5]) != 0.9622548560412576:
    print('reg.predict failed on input [5,5]')
