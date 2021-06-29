###La funcion filter 
## aplica la funcion a todos los elementos de un objeto iterable 
##Devuelve un objeto generado de ahiq eu usemos las funcion list() para convertirlo a lista 
### Duvuelve  los elementos para los cuales aplicar la funcion devuelve un true

nums = [49, 57, 62, 147, 2101, 22]
print(list(filter(lambda x: (x % 7 == 0), nums)))


## Ejemplo con funcion --- combinar la funcion filter con una funcion 
def third_letter_is_s(word):
  return word[2] == "s"

words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(list(filter(third_letter_is_s, words)))

###Ejercicio con funciones lambda

nums = [-5,-3,5,2,6,9,8,9,-6,8,7,6,9,-6,-2,-1]

print(list(filter(lambda x: x > 0,nums)))