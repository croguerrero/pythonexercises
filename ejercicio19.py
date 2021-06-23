client = {}
print("Introduzca el nombre del cliente: ")
client["name"] = str(input())
print("Introduzca los apellidos del cliente: ")
client["surname"] = str(input())
print("Introduzca la edad del cliente: ")
client["age"] = int(input())
print("Introduzca el DNI del cliente: ")
client["dni"] = str(input())
print("Introduzca el total a pagar del cliente: ")
client["total"] = float(input())

print(client)