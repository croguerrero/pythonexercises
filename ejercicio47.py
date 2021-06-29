##Crea una función que dados dos números reales por parámetro, devuelve el mayor.
def helper(a,b):
        print("El numero {} es mayor que {}".format(a,b))
    
def mayor(a,b):
    if a > b:
        helper(a,b)
    else:
        helper(b,a)

### funcion que los divisores del numero 

def divisores(num):
   div = []
   for i in range(1,num + 1):
       if num % i == 0 :
           div.append(i)
   return print(div)
        

divisores(48)
