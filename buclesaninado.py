##Bucles anidados y mediante tablas de multiplicar

for i in range(1,11):
    print("\n Tabla de multiplicar del {}".format(i))
    for j in range (1,11):
        print("{} x {} = {}".format(i,j,i*j))