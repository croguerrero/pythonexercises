n = float(input("Introduce un numero: "))

sum = 0

while n != 0:
    sum += n
    n = float(input("Introduce un numero: "))
else:
    print("La suma es: " ,sum)
