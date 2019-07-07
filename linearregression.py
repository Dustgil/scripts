import numpy as np

# input data
data = [[0,1],[1,3],[2,4],[3,4]]


# create matrix
A = np.array([1,1]) # starting row to make dimensions work for cleaner code.
for point in data:
    row = [1, point[0]]
    A = np.vstack([A, row])

A = np.delete(A, (0), axis=0) # delete starting row to get correct matrix

T = A.transpose()

TA = np.matmul(T, A)
inv = np.linalg.inv(TA)

l = []
for e in data:
    l.append(e[1])

y = np.array(l)
y = y.transpose()



v = np.matmul(inv, T)
v = np.matmul(v, y)

print(v)
