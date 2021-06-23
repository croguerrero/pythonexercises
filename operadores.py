isadult= True
print(type(isadult))

A = True
not A

A, B = True, True
print(A and B)

print((not A) or (not B))

edad = 41

print((edad >= 16) and (edad <= 40))

print("Marcelo" <= "Paola")

s="Mallorca es una isla preciosa"
print(s.startswith("m"))  ## busca nos devuelve True si la cadena empieza con el caracter indicado
print(s.endswith("a"))
print(s.isalnum) # metodo para saber si todos los caracteres de la cadena son alfanumericos
print(s.isalpha) # metodo que comprueba si existenn caracteres alfanumeros no se considera espacios en blanco y caracteres especiales
p = "123"
print(p.isdigit()) # nos devuelve para saber si el usario digita o introduce digitos
p = "        "
print(p.isspace()) # saber se introdujeron espacios
p="hola"
print((p.islower())) # saber si estan en minusculas
print(p.isupper()) # saber si estan en mayusculas
print(p.istitle()) # saber si tiene la cadena empiezan con mayusculas





