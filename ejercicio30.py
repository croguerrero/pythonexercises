## comprobar el elemento maximo de un conjunto sin utilizar la funcion max()
myset = {2,5,6,8,9,8,9,6,66,6,6,66,6,103,10,6}
max = -9999

for e in myset:
    if e > max:
        max = e

print("El numero maximo de {} es {} ".format(myset,max))