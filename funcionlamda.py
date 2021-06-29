##Funciones lamda
##Solo se puede hace una linea de codigo 
## Puede contener cualquier numero de argumentos

plus10 = lambda x: x + 10   ### se utiliza en juegos o analisis de datos

prod = lambda x, y: x*y
print(prod(5,6))

dicrim = lambda a, b, c: ((b**2)-(4*a*c)) ## crea una funcion lambda encuentra el discriminante de una ecuacion 

####Ejercicio

doble_square = lambda x:(x,2*x,x**2) ## linea de codigo de la funcion a ejecutar, crea una tupla

print(doble_square(4))

##Ejericio 1: Crea una función lambda que dado un número entero multiplique por su anterior y su siguiente. Por ejemplo,
##si proporcionamos n = 3, nos tendrá que devolver 2 · 3 · 4 = 24.
multiplicador = lambda x : ((x-1)*x*(x+1))
print(multiplicador(3))

### Ejericio 2: Crea una función lambda que dados dos números devuelva si el primero es mayor.

 
mayorq = lambda x, y : x if x > y else y
print(mayorq(88,6))

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

print(list(filtrado))