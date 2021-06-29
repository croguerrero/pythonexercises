### Docstring documentacion 
## Siempre van entre comillas triples

def euclidean_division(x, y):
  """
  Esta función calcula el cociente y el resto de la
  división entera de x entre y.

  Args:
    x (int): dividendo
    y (int): divisor (! de cero)

  Returns:
    (q, r): tupla con el valor de (cociente, resto)
  """
  q = x // y
  r = x % y
  return q, r

## Para acceder el docstring y revisarlo 
print(euclidean_division.__doc__)