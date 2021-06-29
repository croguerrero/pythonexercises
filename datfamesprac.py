###Dataframes es una estructura bidimensional mutables de datos con los ejes etiquetados
##   cada fila representa una observacion diferente
###  cada columna representa una variable

### pandas 
import pandas as pd 

### Datframes a partir de un diccionario

data = {"x":[1,2,3,4,5], "y":[2,4,6,8,10]}
df1 = pd.DataFrame(data=data)

##print(df1)

## Vamos a crear de una lista de listas

df2= pd.DataFrame(data = [[1,2],[2,4],[3,6],[5,10]], 
                            columns=["x","y"])
##print(df2)

### Ejemplo3 :  Vamos a crear el mismo dataframe de 5 filas y 
# 2 columnas, con la diferencia de que vamos a modificar el nombre de las filas.
df3 = pd.DataFrame(data = data, index = ["obs1", "obs2", "obs3", "obs4", "obs5"])
##print(df3)


## Las claves de los diccionarios deben coincidir para crear el dataframe
d = {"a": [1, 2, 3],
     "b": [4, 5, 6],
     "b1": [7, 8, 9]}
df = pd.DataFrame(d, columns = ["a", "b", "b1"]) 
##print(df)

## Ejemplo 3: Crear un dadtaframe a partir deuna lista de diccionarios

data = [{"x": 1, "y": 2},
        {"x": 2, "y": 4},
        {"x": 3, "y": 6},
        {"x": 4, "y": 8},
        {"x": 5, "y": 10}]
df4 = pd.DataFrame(data = data)
#print(df4)

## Ejemplo: Con la funcion zip()

x = [1,2,3,4,5]
y = [2,4,6,8,10]
data = list(zip(x,y))
#print(data)
df5 = pd.DataFrame(data, columns=["x","y"])
#print(df5)


########## El metodo creando dataframes con .from_dict() te ayuda para crear y las claves representar una fila #####

d = {"a": [1, 2, 3],
     "b": [4, 5, 6],
     "b1": [7, 8, 9]}

df6 = pd.DataFrame.from_dict(d)


d = {"fila1": [1, 4, 7],
     "fila2": [2, 5, 8],
     "fila3": [3, 6, 9]}
df7 = pd.DataFrame.from_dict(d, orient = "index", columns = ["A", "B", "C"])
print(df7)