import numpy as np

n = int(input("Introduce las filas: "))
m = int(input("Introduce las columnas: "))

A = np.empty((n,m))

print("/n=======Matriz A========")

for i in range(n):
    for j in range(m):
        A[i, j] = float(input("Introduce el elemento ({},{})".format(i, j)))


B = np.empty((n,m))

print("/n=======Matriz B========")

for i in range(n):
    for j in range(m):
        B[i, j] = float(input("Introduce el elemento ({},{})".format(i, j)))

C = A + B
print(C)