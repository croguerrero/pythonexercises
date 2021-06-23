s = input("Introduce una frase: ")
counted = []
letters = {}

s = s.lower()
for c in s:
  if c not in counted and c != " ":
    counted.append(c)
    letters[c.upper()] = s.count(c)

print(letters)