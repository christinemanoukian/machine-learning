import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor

reg = LogisticRegressor(0, 10)
data = [[0,0,1], [1,0,2], [2,0,4], [4,0,8], [6,0,9], [0,2,2], [0,4,5], [0,6,7], [0,8,6], [2,2,1], [3,4,1]]
interaction_terms = True
reg.fit(data, interaction_terms)
if reg.coefficients != [-.74, -.38, .35, 2.06]:
    print('reg.coefficients failed on input [[0,0,1], [1,0,2], [2,0,4], [4,0,8], [6,0,9], [0,2,2], [0,4,5], [0,6,7], [0,8,6], [2,2,1], [3,4,1]]')
if reg.predict([5,5]) != 9.7:
    print('reg.predict failed on input [5,5]')
if reg.predict([5,0]) != 8.4:
    print('reg.predict failed on input [5,0]')
