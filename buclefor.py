s ="hola como vas "

for c in s:
    print(c)

valor = 0

for i in range (1,11,2): # for tiene tres paso for range(start, stop, step) tambien se puede hacer en negativ
    valor = valor + i    

print(valor)

for i in range (11,0,-1):
    print(i)

for i in range (101):
    if i % 2 == 0 or i % 5 ==0:
        continue   # no corta el bucle puede ir con while y for
    print(i)