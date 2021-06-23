## vamos a sumar matrices propocionadas por el usuario
n = int(input("Numero de filas de las matrices: "))
m = int(input("Numero de columnas de las matrices: "))

A = []
print("/n=======Matriz A========")

for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input("Introduce el elemento ({},{})".format(i,j))))

B = []
print("/n=======Matriz B========")

for i in range(n):
    B.append([])
    for j in range(m):
        B[i].append(float(input("Introduce el elemento ({},{})".format(i,j))))

C=[]

for i in range(n):
    C.append([])
    for j in range(m):
        C[i].append(A[i][j]+B[i][j])

print("/n=======Matriz A + B========")

for i in range(n):
  for j in range(m):
    print(C[i][j], end = "  " if C[i][j] >= 0 else " ")
  print("")