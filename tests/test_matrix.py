import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1,2], [3,4]])
other_matrix = Matrix([[1,1], [1,1]]) 
other_matrix_2 = Matrix([[2,2], [2,2]]) 
At = A.transpose()
Aat = A.add(At)
Aa = A.add(other_matrix)
As = A.subtract(other_matrix)
Asm = A.scalar_multiply(2)
Am = A.matrix_multiply(other_matrix_2)
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

B = Matrix([[1,2,3], [4,5,6]])
other_matrix = Matrix([[1,1,1], [1,1,1]])
other_matrix_2 = Matrix([[2,2,2], [2,2,2]])
Bt = B.transpose()
Ba = B.add(other_matrix)
Bs = B.subtract(other_matrix)
Bsm = B.scalar_multiply(2)
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

C = Matrix([[1,2], [3,4], [5,6]])
other_matrix = Matrix([[1,1], [1,1], [1,1]])
other_matrix_2 = Matrix([[1,2,3,4], [3,4,1,5]])
Ct = C.transpose()
Ca = C.add(other_matrix)
Cs = C.subtract(other_matrix)
Csm = C.scalar_multiply(2)
Cm = C.matrix_multiply(other_matrix_2)
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
Da = D.add(other_matrix)
Ds = D.subtract(other_matrix)
Dsm = D.scalar_multiply(9)
Dm = D.matrix_multiply(other_matrix_2)
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

F = Matrix([[2,5,2,2], [6,7,6,6], [2,5,5,5], [3,8,8,3]])
if F.calc_determinant() != 1030:
    print('failed to calculate determinant')

G = Matrix([[3,1], [6,2]])
if G.calc_determinant() != 0:
    print('failed to calculate determinant')

H = Matrix([[1,2], [4,3], [4,1]])
if H.calc_determinant() != 'cannot find determinant':
    print('failed to calculate determinant')
