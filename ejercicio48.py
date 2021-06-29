###Escriba un programa que permita crear dos listas de palabras y que, 
## a continuación, elimine de la primera lista los nombres de la segunda lista.

def llenarlista(numero):
    lista = []
    for i in range(numero):
        nombre=input("Ingrese un nombre de la lista: ")
        lista.append(nombre)
    return print("Lista creada: ",lista)


numero = int(input("Dígame cuántas palabras tiene la lista: "))
llenarlista(numero)

    

##delete: int(print("Cuantos nombres de la lista quiere eliminar: "))

