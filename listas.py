#Ejemplo de Listas //Heterogeanes y Mutables
l = ["Juan", 31, 172.32, True]
print(type(l))
print(len(l))
print(l[0])

#Elementos de una lista--podemos acceder por la posicion de la lista []
print(l[0])
print(l[-1])   # me devuelve ultimo valor de la lista
print(l[:2])  # varios valores de la lista
print(l[2:])

# cambiar el valor de la lista

l[0]= "Pedro"
print(l)

#Metodo  .append() agrega un elemento al final de la lista
l.append(34)
l.append("Tomas")

print(l)

# Metodo agrega un elemento en la posicion especifica .insert() y no lo modifica

l.insert(0,"Juan")
l.insert(6,12334)
print(l)
