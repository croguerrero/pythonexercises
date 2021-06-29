## Funcion helper ayuda a reducir el tamano del codigo
def helper_print(x, y, sign):
  print("El resultado de sumar {} más {} es {}.".format(x, y, sign))

def sign_sum(x, y):
  if x + y > 0:
    helper_print(x, y, "positivo")
  elif x + y == 0:
    helper_print(x, y, "cero")
  else:
    helper_print(x, y, "negativo")

sign_sum(5,4)
sign_sum(5,-5)
sign_sum(-5,4)


