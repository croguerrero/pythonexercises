import numpy as np

n = int(input("Introduce las filas A: "))
m = int(input("Introduce las columnas A: "))
p = int(input("Introduce las columnas B: "))

A = np.empty((n,m))

print("\n=======Matriz A========")

for i in range(n):
    for j in range(m):
        A[i, j] = float(input("Introduce el elemento ({},{})".format(i, j)))


B = np.empty((m,p))

print("\n=======Matriz B========")

for i in range(m):
    for j in range(p):
        B[i, j] = float(input("Introduce el elemento ({},{})".format(i, j)))

print("\nMatriz A * B")
print(A.dot(B))