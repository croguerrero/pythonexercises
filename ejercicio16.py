import numpy as np

n = int(input("Introduce las filas: "))
m = int(input("Introduce las columnas: "))

A = np.empty((n,m))

for i in range(n):
    for j in range(m):
        A[i, j] = float(input("Introduce el elemento ({},{})".format(i, j)))

print("\n======MATRIZ A========")
print(A)