##Imprimir todos los números entre el 100 y el 199.
frase = input("Escriba la frase: ")
frase.lower()
for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
     print("Esta es la vocal: {}".format(i))

r =0
for j in range(1,101,3):
    r += j
    
print("La suma total es:",r)