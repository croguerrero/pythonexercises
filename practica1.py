##Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key ="saga"
passw=input("Introduce el password aqui: ")
if key == passw.lower():
    print("La paswd coincide")
else:
    print("El passs no coincide")


####### Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n= float(input("Introduce un numero: "))

if n%2==0:
    print("El numero {} es par".format(n))
else:
        print("El numero {} es inpar".format(n))

###Para tributar un determinado impuesto se debe ser mayor de 16 años y 
## tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte 
## al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad=int(input("Ingrese su edad: "))
mensual=int(input("Ingrese su sueldo: "))

if edad >=16 and mensual >= 1000:
    print("Ud tiene {} de edad y un sueldo de {}, lo cual le posibilita para tributar".format(edad,mensual))
else:
    print("Ud tiene {} de edad y un sueldo de {}, lo cual no le posibilita para tributar".format(edad,mensual))
