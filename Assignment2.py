import numpy as np

mat = np.matrix('3 11 6 5; 4 7 10 2; 13 9 0 8')
print(mat)
mat[2, 0] = 20
print(mat)
print(mat[1, 3]-mat[0, 1])
v = np.matrix('4 15 8 12 34 2 50 23 11')
u = v[0, 2:6]
print(u)
B = mat[:, 2]
print(B)
C = mat[2, :]
print(C)
F = mat[1:3, 1:3]
print(F)
