b = 0.02

if b > 0.1:
    print(True)
else:
    print(False)


s = "Mi gato mola mucho pasma lento"
c = " "

if c in s:
    print("El string tiene {} espacios en blanco".format(s.count(c)))


A = float(input("Coeficiente A = "))
B = float(input("Coeficiente B = "))

if A != 0:
    sol= -B/A
    print("La solucion es x=" , sol)
elif B > 3:
    print("hola")
else:
    print("No hay ecuacion que resolver, por que A = 0")
