import sys
sys.path.append('src')
from matrix import Matrix

def calc_coefficients(data):
    y = []
    for lst in data:
        row = []
        row.append(lst[len(lst)-1])
        y.append(row)
    y = Matrix(y)
    A = []
    for lst in data:
        lst.remove(lst[len(lst)-1])
        lst.insert(0, 1)
        A.append(lst)
    A = Matrix(A)
    At = A.transpose()
    Aty = At.matrix_multiply(y)
    AtA = At.matrix_multiply(A)
    AtA_inverse = AtA.inverse()
    result = AtA_inverse.matrix_multiply(At)
    result = result.matrix_multiply(y)
    return result

#data = [[0,0,1], [1,0,2], [2,0,4], [4,0,8], [6,0,9], [0,2,2], [0,4,5], [0,6,7], [0,8,6]]
#calc_coefficients(data).print()
#coefficients = [1.149350649350646, 1.4220779220779225, 0.7584415584415587]
#b_0 = coefficients[0]
#b_1 = coefficients[1]
#b_2 = coefficients[2]
#five_and_zero = b_0 + b_1*5 + b_2*0
#print(five_and_zero)
#five_and_five = b_0 + b_1*5 + b_2*5
#print(five_and_five)
