word = ["ola","carola", "pina"]
f_leters = []

for w in word:
    f_leters.append(w[0])

print(tuple(zip(word, f_leters)))