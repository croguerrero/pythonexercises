n = int(input("Introduce el tamano de la lista: "))

l =[]

for i in range(n):
    l.append(int(input()))

print("Esta es tu lista:",l)

for i in l:
    print(i)