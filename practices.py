##Ejercicios

#//1

print("Introduce una palabra y yo te la devuelvo en mayuscula")
word=input()
print(word.upper())

#2 Devolver la frase con todas las palabras empezando con mayuculas
print("Introduce una frase y yo te devuelvo todas las palabras empezando en mayúscula")
s = input()
print(s.title())

#3 Devolver la palabra (con 3 o más letras) con todas las letras en minúscula salvo la tercera letraprint("Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera")
print("Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera")
word = input()
word = word[:2].lower() + word[2].upper() + word[3:].lower()
print(word)

#4 Introduce una palabra y yo te devuelvo todas sus letras en mayusculas salvo la primera y la ultima 
print("Intorduce una palabra y yo te devuelvo todas sus letras en mayusculas slavo la primera y la ultima")
word=input()
word=word[0].lower() + word[1:(len(word)-1)].upper() + word[-1].lower()
print(word)

#5 Devolver la frase donde cada vez que aparezcan las dos primeras letras de la primera palabra, sean sustituidas por cualesquiera otras letras
sub="mi"
print("Intorduce una palabra y yo te devuelvo todas sus letras en mayusculas slavo la primera y la ultima")
word=input()
print(word.replace(word[:2], sub))