import numpy as np 
A = np.empty((2, 3))
B = np.empty_like(A)
print(A)
print(B)

c = np.zeros((3, 5))
d = np.zeros_like(A)
print(c)
print(d)

e = np.ones((1, 4))
print(e)

d = np.ones_like(B)
print(d)

##ejercicio con numpy

M = np.matrix([[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]])
B = np.matrix([[-1, -2, 0, 6], [-2, 3, 0, 9], [0, 0, -3, 5]])
A = np.matrix([[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]])
C = np.matrix([[-1, -2, 0], [-2, 3, 0], [0, 0, -3], [1, 1, -1]])
matrixsum = M + B
matrixprod = A.dot(C)
print(matrixsum)
print(matrixprod)