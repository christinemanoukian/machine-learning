import sys
sys.path.append('src')
from matrix import Matrix

print('test1')
A = Matrix([[1,2], [3,4]])
A.print()
At = A.transpose()
At.print()
A.add(At).print()
other_matrix = Matrix([[1,1], [1,1]]) 
A.add(other_matrix).print() # should print [[2,3], [4,5]]
A.subtract(other_matrix).print() # should print [[0,1], [2,3]]
A.scalar_multiply(2).print() # should print [[2,4], [6,8]]
other_matrix_2 = Matrix([[2,2], [2,2]]) 
A.matrix_multiply(other_matrix_2) # should print [[6,6], [14,14]]

print('test2')
B = Matrix([[1,2,3], [4,5,6]])
B.print()
Bt = B.transpose()
Bt.print()
other_matrix = Matrix([[1,1,1], [1,1,1]])
B.add(other_matrix).print() # should print [[2,3,4], [5,6,7]]
B.subtract(other_matrix).print() # should print [[0,1,2], [3,4,5]]
B.scalar_multiply(2).print() # should print [[2,4,6], [8,10,12]]
other_matrix_2 = Matrix([[2,2,2], [2,2,2]])
B.matrix_multiply(other_matrix_2) # should print 'cannot multiply matrices'

print('test3')
C = Matrix([[1,2], [3,4], [5,6]])
C.print()
Ct = C.transpose()
Ct.print()
other_matrix = Matrix([[1,1], [1,1], [1,1]])
C.add(other_matrix).print() # should print [[2,3], [4,5], [6,7]]
C.subtract(other_matrix).print() # should print [[0,1], [2,3], [4,5]]
C.scalar_multiply(2).print() # should print [[2,4], [6,8], [10,12]]
other_matrix_2 = Matrix([[1,2,3,4], [3,4,1,5]])
C.matrix_multiply(other_matrix_2) # should print [[7,10,5,14], [15,22,13,32], [23,34,21,50]]