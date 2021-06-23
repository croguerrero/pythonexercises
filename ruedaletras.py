n = int(input("Introduce una rotacion: "))
i = 65

while i <= 90:
    if i + n <= 90:
        print(chr(i) + " : " + chr(i + n)) ## la funcion chr() tranforma a caracter dado un numero
    else:
               print(chr(i) + " : " + chr((i-26) + n))
    i += 1
 