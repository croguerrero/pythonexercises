A = [[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]]
B = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3], [1, 1, -1]]

m, n, p = len(A), len(B), len(B[0])

C = []

for i in range(m):
  C.append([])
  for j in range(p):
    elemento = 0
    for k in range(n):
      elemento = elemento + A[i][k] * B[k][j]
    C[i].append(elemento)

for row in C:
    print(row)