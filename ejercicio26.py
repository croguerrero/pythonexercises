word1 = input("Palabra 1")
word2 = input("Palabra 2")

letter1 = set()
letter2 = set()

for l in word1.lower():
    letter1.add(l)

for l in word2.lower():
    letter2.add(l)

common = letter1 & letter2 ## Calculo de la Interseccion de dos conjuntos
print(common)
