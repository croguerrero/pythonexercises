#### la funcion sorted()
### Ordena los elementos del objeto iterable que indiquemos de acuerdo a la función que pasemos por parámetro
####  Como output, devuelve una permutación del objeto iterable ordenado según la función indicada


##Ejercicio: Con la ayuda de las funciones lambda, apliquemos sorted() para ordenar la lista words en función 
# de las longitudes de las palabras en orden descendente.
words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
print(sorted(words, key = lambda x: len(x), reverse = True))

print(sorted(words, key = len, reverse = True))

print(sorted(words, key = len))
print(words)