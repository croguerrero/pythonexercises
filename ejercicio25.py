s = input("Introduce una frase: ")
letters = set()

for c in s.lower():
    if c != " ":
        letters.add(c)

print(letters)