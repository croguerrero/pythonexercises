print("Indica el destinitario de la canción:")
name = input()

s1 = "¡Cumpleaños feliz!"
s2 = "Te deseamos todos"

song = (s1 + "\n") * 2 + s2.replace("todos", name) + ",\n" + s1
print(song)