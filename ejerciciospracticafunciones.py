def area_rectangulo(base,altura):
    """
        Calcula el area del rectangulo

    Arg:
        base y altura (int or float)
    Return:
        area(Float)
    """
    if base > 0 and altura > 0:
        area = base * altura
    else: 
        print("Los parametos ingresados de base y altura no son los correctos")
        area = 0 
    return print("Esta es el area del rectangulo {}".format(area))

##area_rectangulo(1.5,6.5)

def area_circulo(r):
    """
        Calcula el area del circulo

    Arg:
        radio (int or float)
    Return:
        area(Float)
    """
    import math
    A = (r**2)*(math.pi)
    return print("El area del circulo es: {}".format(A))

##area_circulo(5)

def relacion(a,b):
     """
        Calcula la relacio de dos numeros

    Arg:
        Dos numeros enteros a y b (int)
    Return:
        1 A>B
       -1 B>A
        0 A=B
    """
     if a > b:
        r = 1
     elif b > a:
        r = -1
     else:
        r = 0
     return print("La relacion de los numero a y b es igual: {}".format(r))

##relacion (5,10)

def separar(*lista):
    """
        Dada un lista separa en numeros pares e impares

    Arg:
        Indeterminado lista de numeros
    Return:
        Lista pares[] en formaa ordenada
        Lista impares[] en forma ordenada
    """
    pares = []
    impares = []
    for i in lista:
        rest = i % 2
        if rest==0:
            pares.append(i)
        else:
            impares.append(i)
    return print("Lista pares: {}".format(sorted(pares))) , print("Lista impares: {}".format(sorted(impares)))


separar(6,5,2,1,7,8,9,88,66,55,66,105,100,1,3,9,7,26,44,65665,55)

