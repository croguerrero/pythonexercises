##Variables de un funcion 
## Hay dos variables local y global, local solo dentro de la funcion y global es en el entorno global 

def arit_ope(x,y):
    suma = x + y
    diff = x - y 
    prod = x * y
    div = x * y
    return print({"Suma: ", suma,
            "Prod: ", prod,
            "Diff: ", diff,
            "Div: ", div})

arit_ope(5,5)
## debes utilizar la palabra global para asignar 

n = 7

def next_n():
    global n
    return n + 1

print(next_n())

## Paso por copia vs paso por referencia
##Paso por copia
def double_v(n):
    n = n * 2
    return n 
num = 5
print(double_v(num))
print(num)

## Paso por referencia

def double_ref(ns):
    for i, n in enumerate(ns):
        ns[i] *= 2
    
    return ns

nums = [1,2,3,4,5]
print(double_ref(nums))
print(nums)

## En el caso q no se requiere modificacion y necesite la copia original 
nums = [1,2,3,4,5]
print(double_ref(nums[:]))  ## aqui se le pasa un copia de la lista
print(nums)
