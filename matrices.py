matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])

## manera de imprimir una matrix de forma tabular con un for

for row in matrix:
    print(row)

## manera de imprimir todos los elementos de la matriz con dos for aninados

for row in matrix:
    for element in row:
        print(element)

## si queremos mostrar la matriz de forma de tabla sin comas 

m = len(matrix)
n = len(matrix)

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print("")
"/n"
for row in matrix:
    for element in row:
        print(element, end = " ")
    print("")