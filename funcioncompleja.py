from typing import Container


def euclidean_division(x, y):
  ints = (x == int(x)) and (y == int(y))
  
  if not ints:
    x = int(x)
    y = int(y)
    print("Se tomarán como parámetros la parte entera de los valores introducidos.")
  
  if abs(x) >= abs(y):
    q = x // y
    r = x % y
    print("Se ha realizado la división {} entre {} y se ha obtenido como cociente q = {} y como resto, r = {}".format(x, y, q, r))

  else:
    q = y // x
    r = y % x
    print("Se ha realizado la división {} entre {} y se ha obtenido como cociente q = {} y como resto, r = {}".format(y, x, q, r))


  return q, r


### Ejemplos 
##

def sing(num):
    """
        Funcion dado un numero comprueba su signo 
        Args: 
         num(int): numero del cual podemos hallar su signo

        Return:
            String() que indica el signo
    """
    if num > 0:
        print(" Este es un numero postivo {}".format(num))
    elif num < 0:
        print(" Este es un numero negativo: {}".format(num))
    else :
        print(" Este es un numero es: {}".format(num))


def tabla(num):
    """
    Dado un número entero, imprimimos su tabla de multiplicar con
    los 10 primeros múltiplos y devolvemos una lista de los múltiplos. 

  Args:
    num (int): valor del cual vamos a calcular sus tabla de multiplicar

  Returns: 
    multiples (list): lista con los 10 primeros múltiplos de num
  """
    if type(num) != type(1):
        print("El numero introducido no es entero")
        return
    multiples = []
    print("La tabla de multiplicar del {}:".format(num))
    for i in range (1,11,1):
        prod = i * num
        print("{} x {} = {}".format(i,num, prod))
        multiples.append(prod)
    return multiples

#### Ejemplo 7

def cointain_a(sentence):
    """
    Dado un frase comprueba si existe la letra a 

    Arg:
         sentence(string) frase para verificar

    Return:
         Indica True o False si contiene o no la letra 'a'
    """
    i = 0 
    while sentence[i] != ".":
        if sentence[i] == "a":
            return print(True)
        i +=1
    return print(False) 
cointain_a("Hol que ms.")

def cointain_letter(sentence):
    """
    Dado un frase comprueba si existe la letra a 

    Arg:
         sentence(string) frase para verificar

    Return:
         Indica True o False si contiene o no la letra 'a'
    """
    print("Dada la oracion: ", sentence )
    sentence = sentence.lower()
    letter = input("Indicar que letra quiere encontrar: ")
    i = 0 
    while sentence[i] != ".":
        if sentence[i] == letter:
            return print(True)
        i +=1
    return print(False) 

cointain_letter("Hol que ms.")
