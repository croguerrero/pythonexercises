s = input(" Ingrese un frase: ")
s.lower()
vowels = ["a", "e", "i", "o", "u"]

vowels_count = 0
consonants_count = 0
blanks_count = 0

for c in s:
    if c in vowels:
        vowels_count += 1
    elif c.isalpha():
        consonants_count += 1
    elif c == " ":
        blanks_count += 1
    
info = [("# Vocales: ", vowels_count), ("# Consonantes: ", consonants_count),("# Espacios: ", blanks_count) ]

print(info)