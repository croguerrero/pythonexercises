### Triangulo de pascal 
def chosse(n,k):
    """
    Calcula el numero combinario n sobre k
    """
    import math 
    if (n>=k and k>=0):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    else:
        return "No se puede calcular el numero factorial indicado"

def pascalt(n=1):
    print(1)
    for i in range(1, n +1 ):
        for k in range(i + 1):
            print(chosse(i,k), end = " ")
        print("")

pascalt(15)