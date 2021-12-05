import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1,2], [3,4]])
other_matrix = Matrix([[1,1], [1,1]]) 
other_matrix_2 = Matrix([[2,2], [2,2]])
other_matrix_3 = Matrix([[1,2], [3,4]]) 
At = A.transpose()
Aat = A + At
Aa = A + other_matrix
As = A - other_matrix
Asm = A * 2
Am = A @ other_matrix_2
Ae = A ** 2
check_for_equality = A == other_matrix_3
if At.elements != [[1,3], [2,4]]:
    print('Actual matrix does not equal intended matrix') 
if Aat.elements != [[2,5], [5,8]]:
    print('Actual matrix does not equal intended matrix') 
if Aa.elements != [[2,3], [4,5]]:
    print('Actual matrix does not equal intended matrix')
if As.elements != [[0,1], [2,3]]:
    print('Actual matrix does not equal intended matrix')
if Asm.elements != [[2,4], [6,8]]:
    print('Actual matrix does not equal intended matrix')
if Am.elements != [[6,6],[14,14]]:
    print('Actual matrix does not equal intended matrix')
if Ae.elements != [[7, 10], [15, 22]]:
    print('Actual matrix does not equal intended matrix')
if check_for_equality != True:
    print('test failed')

B = Matrix([[1,2,3], [4,5,6]])
other_matrix = Matrix([[1,1,1], [1,1,1]])
other_matrix_2 = Matrix([[2,2,2], [2,2,2]])
other_matrix_3 = Matrix([[1,2,3], [4,5,5]])
Bt = B.transpose()
Ba = B + other_matrix
Bs = B - other_matrix
Bsm = B * 2
check_for_equality = B == other_matrix_3
if Bt.elements != [[1,4], [2,5], [3,6]]:
    print('Actual matrix does not equal intended matrix')
if Ba.elements != [[2,3,4], [5,6,7]]:
    print('Actual matrix does not equal intended matrix')
if Bs.elements != [[0,1,2], [3,4,5]]:
    print('Actual matrix does not equal intended matrix')
if Bsm.elements != [[2,4,6], [8,10,12]]:
    print('Actual matrix does not equal intended matrix')
if B.matrix_multiply(other_matrix_2) != 'cannot multiply matrices':
    print('failed')
if check_for_equality != False:
    print('test failed')

C = Matrix([[1,2], [3,4], [5,6]])
other_matrix = Matrix([[1,1], [1,1], [1,1]])
other_matrix_2 = Matrix([[1,2,3,4], [3,4,1,5]])
Ct = C.transpose()
Ca = C + other_matrix
Cs = C - other_matrix
Csm = C * 2
Cm = C @ other_matrix_2
if Ct.elements != [[1,3,5], [2,4,6]]:
    print('Actual matrix does not equal intended matrix')
if Ca.elements != [[2,3], [4,5], [6,7]]:
    print('Actual matrix does not equal intended matrix')
if Cs.elements != [[0,1], [2,3], [4,5]]:
    print('Actual matrix does not equal intended matrix')
if Csm.elements != [[2,4], [6,8], [10,12]]:
    print('Actual matrix does not equal intended matrix')
if Cm.elements != [[7,10,5,14], [15,22,13,32], [23,34,21,50]]:
    print('Actual matrix does not equal intended matrix')

D = Matrix([[1,2,3], [4,5,6], [7,8,9]])
other_matrix = Matrix([[0,1,2], [3,4,5], [6,7,8]])
other_matrix_2 = Matrix([[2,3,4], [5,6,7], [8,9,0]])
Dt = D.transpose()
Da = D + other_matrix
Ds = D - other_matrix
Dsm = D * 9
Dm = D @ other_matrix_2
if Dt.elements != [[1,4,7], [2,5,8], [3,6,9]]:
    print('Actual matrix does not equal intended matrix')
if Da.elements != [[1,3,5], [7,9,11], [13,15,17]]:
    print('Actual matrix does not equal intended matrix')
if Ds.elements != [[1,1,1], [1,1,1], [1,1,1]]:
    print('Actual matrix does not equal intended matrix')
if Dsm.elements != [[9,18,27], [36,45,54], [63,72,81]]:
    print('Actual matrix does not equal intended matrix')
if Dm.elements != [[36,42,18], [81,96,51], [126,150,84]]:
    print('Actual matrix does not equal intended matrix')

E = Matrix([[5,5,3], [1,9,6], [6,8,8]])
if E.calc_determinant() != 122:
    print('failed to calculate determinant')

G = Matrix([[3,1], [6,2]])
if G.calc_determinant() != 0:
    print('failed to calculate determinant')

H = Matrix([[1,2], [4,3], [4,1]])
if H.calc_determinant() != 'cannot find determinant':
    print('failed to calculate determinant')

I = Matrix([[4,-3,1], [-2,1,-3], [1,-1,2]])
Ir = I.rref()
if Ir.elements != [[1,0,0], [0,1,0], [0,0,1]]:
    print('Actual matrix does not equal intended matrix')

J = Matrix([[4,-3,1], [-2,1,-3], [-2,1,-3]])
Jr = J.rref()
if Jr.elements != [[1,0,4], [0,1,5], [0,0,0]]:
    print('Actual matrix does not equal intended matrix')

K = Matrix([[3,3.6,0], [5,6,4], [0,0,4]])
Kr = K.rref()
if Kr.elements != [[1,1.2,0], [0,0,1], [0,0,0]]:
    print('Actual matrix does not equal intended matrix')

L = Matrix([[0,1,-2,3], [-1,0,1,-2], [3,-2,5,4]])
Lr = L.rref()
if Lr.elements != [[1,0,0,3], [0,1,0,5], [0,0,1,1]]:
    print('Actual matrix does not equal intended matrix')

M = Matrix([[2,1,1], [3,2,1], [2,1,2]])
Mi = M.inverse()
if Mi.elements != [[3,-1,-1], [-4,2,1], [-1,0,1]]:
    print('failed to calculate inverse')

N = Matrix([[1,2], [3,4], [5,6]])
if N.inverse() != 'no inverse':
    print('failed to calculate inverse')

O = Matrix([[2,3], [4,6]])
if O.inverse() != 'no inverse':
    print('failed to calculate inverse')

P = Matrix([[1,0,0,1], [0,2,1,2], [2,1,0,1], [2,0,1,4]])
Pi = P.inverse()
if Pi.elements != [[-2,-.5,1,.5], [1,.5,0,-.5], [-8,-1,2,2], [3,.5,-1,-.5]]:
    print('failed to calculate inverse')

Q = Matrix([[4,5], [0,1]])
Qi = Q.inverse()
if Qi.elements != [[.25, -1.25], [0,1]]:
    print('failed to calculate inverse')

#E = Matrix([[5,5,3], [1,9,6], [6,8,8]])
if E.determinant_by_rref() != 122:
    print('failed to calculate determinant')

#G = Matrix([[3,1], [6,2]])
if G.determinant_by_rref() != 0:
    print('failed to calculate determinant')

#H = Matrix([[1,2], [4,3], [4,1]])
if H.determinant_by_rref() != 'no determinant':
    print('failed to calculate determinant')