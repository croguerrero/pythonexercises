### Funcion calculador
def calculator(operation, x, y):
  """
  Resuelve la operación aritmética correspondiente para los valores x e y
  Args:
    operation: String que indica la operación aritmética a realizar (sum, subtract, product, division)
    x: Número real
    y: Número real
  Returns:
    result: Número real solución de la operación aritmética indicada para los valores x e y
  """
  operation = operation.lower()
  if operation == "sum":
    result = x + y
  elif operation == "subtract":
    result = x - y
  elif operation == "product":
    result = x * y
  elif operation == "division":
    result = x / y
  else:
    print("Has indicado una operación que esta calculadora no puede resolver.")
    result = "NULL"

  if result != "NULL":
    helper(operation, x, y)
    return result

def helper(operation, x, y):
  """
  Indica la operación realizada e imprime el resultado
  Args:
    operation: String que indica la operación aritmética a realizar (sum, subtract, product, division)
    x: Número real
    y: Número real
  """
  if operation == "sum":
    sign = "+"
  elif operation == "subtract":
    sign = "-"
  elif operation == "product":
    sign = "x"
  elif operation == "division":
    sign = ":"

  print("Se ha realizado la operación {} {} {}".format(x, sign, y))