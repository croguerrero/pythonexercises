## Estructura sin orden que no admiten multiples ocurrencias de un mismos elemento.##
## Pueden ser definidos a partir de la funcion set(), y lo elementos pueden ir entre llaves
## No adminite elementos repetidos
## Los elementos en python son fieles a la definicion matematica de estos

set1 = set([1,2,3,5,6,8,9,])
print(set1)

set2 = set((1,2,3,8,9,7,7,8))
print(set2)

set3 = {1,1,5,6,5,6,8,6,8}
print(set3)

### Subconjuntos
## Metodo para saber si B es subconjunto A .issubset()

A, B = {0,3,7,2,5}, {2,3,0}
B.issubset(A)

print(B <= A)
print(B < A)


## Super conjunto  Un super conjunto A de un conjunto B es un conjunto que contiene B
A, B = {0,3,7,2,5}, {2,3,0}
A.issuperset(B)

print(B >= A)
print(B > A)

### Operaciones con conjuntos 

##Union A u B
print(A | B)
print(A.union(B))

## Intersecion & 
print(A & B)
print(A.intersection(B))

## Diferencia es un nuevo conjunto A que no estan en B

print(A - B)
print(A.difference(B))

## Diferencia Simetrica A y B  A△B=(A∪B)−(A∩B)=(A−B)∪(B−A)
A, B = {0, 1, 4, 5, 8, 13}, {0, 3, 4, 7, 8}
A.symmetric_difference(B)
print((A-B) | (B-A))
print((A | B) - (A & B))

## Bucles en conjuntos itera de la misma 
for item in A:
    print(item)

## Metodo pop() nos devuelve un elemento del conjunto y lo elimina
print(A.pop())

## Metodo cler() vacia el conjunto

print(B.clear())
print(B)