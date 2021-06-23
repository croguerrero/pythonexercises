n1 = int(input("Escriba un numero entero: "))
n2 = int(input("Escriba un numero mayor que {}: ".format(n1)))

while n2 < n1:
    print("\nIntentelo de nuevo ")
    n2 = int(input("Escriba un numero mayor {}: ".format(n1)))

print("Los numeros enteros ingresados son {} , {}".format(n1,n2))

####Escriba un programa que pida números mientras no se escriba un número negativo.
#  El programa terminará escribiendo la suma de los números introducidos.
n = int(input("Escriba un numero: "))
v=0
while n > 0:
    n = int(input("Escriba un numero: "))
    v += n

print("La suma de toda la lista es: {}".format(v))


