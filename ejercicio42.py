## Funcion recursiva cuenta atras 
def countdown(n):
    """
    Cuenta regresiva
    Args:
        n : Numero entero positivo
    Return:
        0 cuando atras ha finalizado
    """
    import time
    if n ==0:
        print("La cuenta regresiva a terminado")
        return print(0)
    time.sleep(1)
    print(n)
    return countdown(n-1)

countdown(10)