## Diferencia simetrica

n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce un numero: "))
n3 = int(input("Introduce un numero: "))
n4 = int(input("Introduce un numero: "))

if n2 < n1 or n4 < n3:
    print("No has proporcionado intervalos")
else:
    n12 = set(range(n1,n2 + 1))
    n34 = set(range(n3,n4 + 1))

print(n12.symmetric_difference(n34)) ## Calcula la diferencia simetira de dos conjuntos