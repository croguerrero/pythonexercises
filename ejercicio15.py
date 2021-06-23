n = int(input("Numero de filas de las matrices A: "))
m = int(input("Numero de columnas de las matrices A: "))
p = int(input("Numero de columnas de las matrices B: "))


A = []
print("/n=======Matriz A========")

for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input("Introduce el elemento ({},{})".format(i,j))))

B = []
print("/n=======Matriz B========")

for i in range(m):
    B.append([])
    for j in range(p):
        B[i].append(float(input("Introduce el elemento ({},{})".format(i,j))))

C = []

for i in range(n):
    C.append([])
    for j in range(p):
        elemento = 0
        for k in range(m):
            elemento += A[i][k] * B[k][j]
        C[i].append(elemento)

print("/n=====Matriz A x B")
for i in range(n):
  for j in range(p):
    print(C[i][j], end = "  " if C[i][j] >= 0 else " ")
  print("")