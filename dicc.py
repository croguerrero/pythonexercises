dicc = {"Jose":32, "Marina":55, "Pedro": 60}
print(dicc)

dicc2= {"names":["Jose", "Marina", "Pedro"], 
         "ages":[32,33,66]
         }
print(dicc2["ages"])

##metodo  .keys() podemos acceder a todas las claves de un diccionario

print(dicc2.keys())
print(dicc2.values())

dicc2["names"] = ["David", "Emilia", "Marcelo"]
dicc2["ages"][2] = 156

print(dicc2)

##################################3
ficha_usuario = {}
print("Introduzca su nombre:")
ficha_usuario["name"] = str(input())
print("Introduzca su edad:")
ficha_usuario["age"] = int(input())
print("¿Es usted una mujer? Responda f en caso afirmativo y m en caso contrario")
ficha_usuario["gender"] = "female" if input() == "f" else "male"
print(ficha_usuario)

##### bucle para el recorrer el diccionario



