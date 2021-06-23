s = "Predecir el futuro resulta un negocio mas o menos rentable"
print("El string original es: ",s)
letter = input("Introduce la letra que quieras: ")

s = s.lower()
letter= letter.lower()

for c in s:
    if c == letter:
        continue
    else:
        print(c, end = "")