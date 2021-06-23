ls = [["hola","marce","como"],
    ['Juan',[1,2,3,4,5],36],
    45]

print(ls)
print(ls[0][1])
print(ls[1][1][4])
##Metododo de listas

# metodo .count()
numbers = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]

counted = []
for element in numbers:
  if element not in counted:
    counted.append(element)
    print("El elemento {} aparece {} veces".format(element, numbers.count(element)))

##metodo .extend()
## UN NUMERO ITERABLE EN PYTHON ES UN OBJETO CAPAZ DE DEVOLVER SUS ELEMENTOS UNO POR UNO
##PERMITIENDO SER ITERADO POR EN UN BUCLE FOR
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.extend([6])
print(numbers)
numbers.extend([7, 8])
print(numbers)
numbers.extend(range(9, 16))
print(numbers)

## .index() recibe un argumento y devuelve el indice de la primera aparicion en la lista

print(numbers.index(4))

## .pop() devuelve el ultimo elemento de la lista y lo borra de la misma 

print(numbers)
for i in range(6):
    print(numbers.pop())
print(numbers)

## .remove() recibe como argumento un elemento y borra su primera apararicion de la lista

numbers.remove(7)
print(numbers)

## .reverse() devuelve la lista en orde inverso

numbers.reverse()
print(numbers)

## .sort() ordena la lista 

numbers.sort()
print(numbers)

### ejemplo de ordenarmiento de lista en forma inversa

numbers.sort(reverse=True)
print(numbers)