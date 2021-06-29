string = "El camino está cerrado pero seguro que podemos encontrar una alternativa"
print("Este es el string original:", end = " ")
print(string)

print("Introduce la palabra que quieras eliminar del string original:")
word = input("Palabra: ")

idx = string.find(word)  ##devolvernos el indice donde aparece
substring = string[:idx] + string[(idx + len(word) + 1):] ##elimina la palabra introducida
print(substring)