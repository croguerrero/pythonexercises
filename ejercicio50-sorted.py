###Ejercicio 
def total_letter(w, l):
  """
  Devuelve el total de apariciones de la letra indicada por parámetro en la palabra w
  Args:
    w: Palabra en formato string
    l: Letra en formato string
  Returns:
    letter: Número entero
  """
  letter = 0
  for c in w.lower():
    if c == l.lower():
      letter += 1
  return letter

#l = input("Introduce una letra: ")
words = ["tutu", "jugueteria", "violonchelo", "fanfarron", "piano", "murcielago"]
#print(sorted(words, key = lambda w: total_letter(w, l), reverse = True))

from numpy import random
print(random.randint(1,21,size = 3))