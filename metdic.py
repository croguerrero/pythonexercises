###metodos para diccionarios
dicc ={"a":4, "b": 6, "c": 8}
print(dicc)

## borra el diccionario
dicc.clear()
print(dicc)

## Copia el diccionario
dicc_copy = dicc.copy()
print(dicc_copy)

### metodo .fromkeys()  recibe como parametro un iterable y un valor y devuelve un diccionario que contiene 
## como claves los elementos del iterable 

dicc = dicc.fromkeys(["a" ,"b" ,"c"],[1, 2, 3, 4])

print(dicc)

## metodo .get() recibe como parametro una clave y devuelve el valor de dicha clave

print(dicc.get("a"))

## metodo .pop() recibe como parametro una clave y la elimina y lo devuelve el valor

print(dicc.pop("b"))
print(dicc)

## .setdefaul() funciona como dos formar como el metodo get() y puede agregar un nuevo elemento
##como get()
print(dicc.setdefault("a"))

## para agregar un elemento
print(dicc.setdefault("h",[1,2,5,6]))
print(dicc)

##metodo update() recibe como parametro otro diccionario en cado de tener claves iguales, actualiza el valor de
# de la clave repetida

dicc1= {"b":[5,6,8,9], "i": [88,99,66,99]} 
dicc.update(dicc1)

print(dicc)

### contruir diccionarios con dict()
l = [["x",1], ["y",2]]
print(dict(l))

dica= dict(x=0,y=1,z=-1)
print(dica)

dicb= dict({"x":1, "y": -1, "z":-2})
print(dicb)

dicd= dict({"x":-2}, y=1, z=-2)
print(dicd)