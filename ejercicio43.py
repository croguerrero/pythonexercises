### Funcion factorial 
def factorial(n):
    """
    Calcula el factorial de un numero positivo
    Args:
     n: Numero positivo 
    Return:
    """
    if n == 0:
       return 1
    return n * factorial(n -1)


print(factorial(6))