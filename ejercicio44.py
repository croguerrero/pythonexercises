### Funcion recursiva serie de Fibonacci()
def fibo(index):
    if index == 0 or index == 1:
        return 1
    return fibo(index -1) + fibo (index - 2)

print(fibo(40))