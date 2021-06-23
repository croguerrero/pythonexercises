
import time

i = 10
print("Preparados para el despegue:")
time.sleep(1)
while i >= 0:
    print(i)
    i -= 1
    if i == 1:
        print("Arrancando propulsores")
    time.sleep(1)
    if i == 0:
        print("Despegue")

else:
    print("La cuenta a terminado")