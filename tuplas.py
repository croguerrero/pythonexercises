t = ("Juan", 32, "Profesor", True)
print(t)
print(type(t))

## O se puede declarar con la funcion tuple()

t = tuple(("Juan", 32, "Profesor", True))
print(t)

## Acceder a elementos de una tupla

print(t[1])
print(t[1:])
print(t[:3])

## para saber si un elemento para saber si un elemento pertenece a una tubla

print(32 in t)

## La tupla es inmutable no se puede modificar 
# Pero si queremos modificar debemos tranformar a lista 

t = list(t)
t[1] = 40
t = tuple(t)

print(t)

## proceso como unpacking 

fruits = "Cereza", "Kiwi", "Pera", "Naranja"
print(type(fruits))

(frut1,frut2,frut3,frut4)= fruits
print(frut1)
print(frut3)

## otra forma de unpacking sin parentesis == Debe coincidir con el numero de frutas
frut1,frut2,frut3,frut4= fruits

print(frut2)
print(frut4)

## El asterisco permite asignar los elementos que sobran en la tupla
(frut1,frut2,*restfruit)= fruits

print(restfruit)

## otro ejemplo 
fruits = "Cereza", "Kiwi", "Pera", "Naranja","Banana", "Manzana"
(frut1,*restfruit,frut2,frut3) = fruits

print(frut1)
print(restfruit)
print(frut4)

## Una manera de no utilizar un elemento de la tupla es con la _ indicando que no necesitas ese elemento

punto = (1,2,3)
x,_,z = punto
print(z+x)

### Las tuplas al sumarse no se modifica la anterior 

## Bucles en tuplas 
fruits = "Cereza", "Kiwi", "Pera", "Naranja", "Melocotón", "Sandía", "Melón"

for fruit in fruits:
  print(fruit)

  ## 2

t = ("cereza", "roja"), ("kiwi", "amarillo"), ("pera", "verde"), ("naranja", "naranja")

for fruit, color in t:
  if fruit == "kiwi":
    print("El color del", fruit, "es", color)
  else:
    print("La {} es {}".format(fruit, color))

## Tuplas y el resto de estructuras

t = [4, 5, 6], {"vowels": ("a", "e", "i", "o", "u")}, {1, 2, 3}, ("x", "y")
print(type(t))

### La funcion zip() permite juntas listas en tuplas, contruye un lista de tuplas, cuando zip debes convertir (diccionario, lista, o tupla)
## CUando se hace zip es un iterador 

objects = ["libreta", "pluma"]
price =[5.00, 3.00]
items = zip(objects, price)
print(items)

print(list(items))

items = zip(objects, price)
print(dict(items))

items = zip(objects, price)
print(tuple(items))

## Se con zip iterar todos los elementos sin necesidad de convertir en (dicc, tuple o lista)
for obj, pr in zip(objects, price):
    print("El objeto {}, cuesta {} $$".format(obj,pr))

##assert True, "El asset fallo" ### Permite realizar comprobacion o testing 
