###Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
#  hasta que el usuario decida terminar. Después se debe 
# mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

cesta = {}
continuar = True

while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    respuesta = input('¿Quieres añadir mas artículos a la lista (Si/No)? ') 
    respuesta.lower()
    if respuesta == "si":
        continuar=True
    else:
        continuar= False
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)