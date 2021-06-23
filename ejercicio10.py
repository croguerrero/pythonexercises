##Dada un lista de caracteres le pediremos al usuario que lemento quiere elminar y lo elminaremos de la lista

ls=["a","b","c","h","h"]
print(ls)
rm=input("Dada la lista cual elemento quiere borrar: ")

for e in ls:
  if e == rm:
    ls.remove(e)
print(ls)

l = ["m", "a", "r", "j", "b", "g", "i", "s", "f", "g","b"]
print("Esta es la lista original:", l)
c = input("Introduce el elemento que quieres eliminar ")

for e in ls:
  if e == c:
    ls.remove(e)

print("Esta es la lista actualizada", ls)