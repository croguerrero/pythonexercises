from typing import Text


age = 15
txtmayor= "Eres mayor"
txtmenor= "Eres menor"

print(txtmayor) if age >= 18 else print(txtmenor)

##Ejercicio 1

n = 8
messaje= "El numero es par" if n % 2 == 0 else "El numero es impar"
print(messaje)

##Ejercicio 2

x = float(input("x = "))
y = float(input("y = "))

if x >= 0 and x <= 1 and y >= 0 and y <= 1:
    print("el punto ({}, {}) se encuentra en cuadrado de la unidad".format(x,y))
else:
    print("el punto ({}, {}) no encuentra en cuadrado de la unidad".format(x,y))

age = int(input("Introduzca su edad: "))
name = input("Introduzca su nombre: ")

if age >= 18:
  if name.startswith("M") or name.startswith("m"):
    print("Eres mayor de edad pues tienes {} años y tu nombre, que es {}, empieza por M".format(age, name))
  else:
    print("Eres mayor de edad pues tienes {} años".format(age))
else:
  print("Eres muy joven")