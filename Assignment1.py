import numpy as np

""" Question 1 """
A = np.matrix('1 3 4 2 ; 2 0 1 6; 4 1 2 7')
print(A)

# Matrix Size
aH = A.shape[0]
aW = A.shape[1]
print(aH)
print(aW)

# Matrix Transpose
Atr = A.transpose()
print(Atr)

print("\nxxxxxxxxxxxxxxxxxxxxxxxxx\n")


""" Question 2 """

B = np.matrix('2 2 3; 4 0 6; 8 1 5')
C = np.matrix('1 1 2; 6 3 5; 1 9 1')

# print(B)
# print(C)

D = np.subtract(B, C)
# print(D)
E = np.add(B, C)
# print(E)
F = np.add(E, 2)
# print(F)
G = B*C
# print(G)
H = np.multiply(B, C)
# print(H)

print("\nxxxxxxxxxxxxxxxxxxxxxxxxx\n")


""" Question 3 """
A1 = np.matrix('2 7 6 8 9 10')
B1 = np.matrix('6 4 3 2 3 4')

C1 = np.multiply(A1, B1)
D1 = np.divide(A1, B1)

# print(C1)
# print(D1)

print("\nxxxxxxxxxxxxxxxxxxxxxxxxx\n")


""" Question 4 """
r1 = np.matrix('7 3 5')
s1 = np.matrix(' 2 4 3')

q1 = np.power(r1, s1)
q2 = np.power(r1, 2)

# print(q1)
# print(q2)

print("\nxxxxxxxxxxxxxxxxxxxxxxxxx\n")

""" Question 5 """

A = np.matrix('1 3 4 2; 2 0 1 6; 4 1 2 7; 0 3 6 4')
print(np.diag(A))
print(A.sum(axis=0))
print(A.sum(axis=1))
print(A.sum())
A[1, :] += 2
A[:, 2] += 2
A[1, 2] -= 2  # Here value was added twice
print(A)
