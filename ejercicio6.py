a0 = int(input("Introduce el termino inicial de una progresion aritmetica: "))
d = int(input("Introduce la diferencia de dicha progresion aritmetica: "))
af = int(input("Indica la cota para finalizar: "))
sum_a=0

for an in range(a0, af + 1, d):
    sum_a += an

print("La suma de los terminos de la sucesion que has indicadoes: ", sum_a) 
