A = [[1, 0, -3], [2, 0, 1], [-1, -1, 0]]
B = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3]]

m = len(A)
n = len(A[0])

if len(A) == len(B) and len(A[0]) == len(B[0]):
  C = []

  for i in range(m):
    C.append([])
    for j in range(n):
      C[i].append(A[i][j] + B[i][j])

  for row in C:
      print(row)

else:
  print("No se puede realizar la suma, pues las dimensiones de las matrices no coinciden.")