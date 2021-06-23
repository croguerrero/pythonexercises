num = int(input("Introduce 1 al 10 "))

while num != 0:
  grade = ""
  if num < 1:
    print("Debes introducir un nunero entero entre 1 y 10")
  elif num < 5:
    grade = "Suspenso"
    print((num, grade))
  elif num < 7:
    grade = "Aprobado"
    print((num, grade))
  elif num < 9:
    grade = "Notable"
    print((num, grade))
  elif num <= 10:
    grade = "Excelente"
    print((num, grade))
  else:
    print("Debes introducir un nunero entero entre 1 y 10")
  num = int(input("Introduce 1 al 10 "))

