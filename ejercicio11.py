reversed = bool(input("Si quieres orden descendente, escribe True. De lo contrario, dale a la tecla Enter: "))
l = []

for _ in range(10):
  l.append(float(input()))

l.sort(reverse = reversed)
print(l)