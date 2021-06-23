## while

i = 1

while i <= 10:
    print(i)
    i += 1

##Ejercicio
s = "paolita ahora mas o menos  "
s = s.lower()
i=0
count= 0
while i < len(s):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count +=1
        i +=1
    else:
        i +=1

print("Tiene {} vocales".format(count))    

