#combinando break y continue
s= "Pensamos demasiado y sentimos muy poco"
letter = input("Introduce una letra: ")
n = int(input("Indica el numero de veces que quieres que aparezca la letra anterior: "))
count= 0
s = s.lower()
letter= letter.lower()

for c in s:
    if count >= n:
        print("\nSe ha superado el limite de aparaciones")
        break
    if c == letter:
        count += 1
    elif c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        continue 

    print(c, end = "")
