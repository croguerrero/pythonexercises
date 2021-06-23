### Funcion en python es una pieza de codigo reutilizable que solo se ejecuta
### cuando es llamada 
## No se puede consultar las variables definidas en la funcion fuera de la funcion

def imprime():
    print("Mi primera funcion")

imprime()

def helloworld():
    print("Hola \nMundo ")

helloworld()

##Ejemplo dos no input pero si outputs
## Ambito de visibilidad de las funciones
def good_mornig():
    greting = "Buenos Dias"
    return greting

print(good_mornig())

## Ejemplo 3 No devuelve nada pero si toma algun parametro

def goodmorning(name):
    print("Buenos Dias, {}!!!!".format(name))

goodmorning("Pepito")

### Ejemplo 4 COntiene entrada y salidas

def euclidiand(x,y):
    q = x // y
    r = x % y
    return q, r
print(euclidiand(x = 41,y = 7))

## Parametros de la funcion python espera las variables que espera

### Numero de arbitriario  de argumentos * con asterisco se puede asignar un numero de variables

def sum_num(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

def pro_num(*numbers):
    prod = 0
    sum = 0
    for n in numbers:
        sum +=n
    prod = sum/len(numbers)
    return prod

print(pro_num(5,6,8,6,8,6,8,7,6,5,6))

## Parametros Hibridos de argumentos 
## Para agregar dos valores o mas
def complete_name(name, **surname):
    print("El nombre completo es {}".format(name), end = " ")
    for i in surname.items():
        print("{}".format(i[1]), end = " ")

complete_name(name ="Marcelo", surname= "Guerrero", surname1 = "Marroquin")

## Parametros por defecto, podemos configurar como se comportara la funcion o los parametros de entrada

def diff(x, y= 1):
    return print("\n",x - y)
diff(45)


