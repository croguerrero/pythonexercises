###La función map()
##Aplica una misma función a todos los elementos de un objeto iterable
##Devuelve un objeto generador, de ahí que usemos la función list() para convertirlo a lista
##Como output, devuelve el resultado de aplicar la función a cada elemento
##Con la ayuda de las funciones lambda, apliquemos map() para calcular las longitudes de las siguientes palabras

words = ["zapato", "amigo", "Yoyo", "barco", "xilófono", "césped"]
print(list(map(lambda w: len(w), words)))

## Mapea funciones por cada elemento como el siguiente ejemplo 
import string 
print(list(map(len,words)))


###Ejercicio de celsios a farenheit

def from_c_f(celsius):
    """
    Convierte de grados celsius a ferenheit

    Arg:
        celsius: Numero Real
    Return:
        farenheit: numer Real
    """
    fare = (celsius*9/5)+32
    return fare

celsius = [5,6,8,6,988,5,88,5,6,6]
print(list(map(from_c_f,celsius)))