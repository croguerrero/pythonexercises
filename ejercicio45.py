###Ecuaciones de primer grado

def equation(A, B):
    """
  Resuelve ecuaciones de primer grado de la forma Ax + B = 0
  Args:
    A: Número real (coeficiente de x)
    B: Número real (término independiente)
  Returns:
    x: Solución de la ecuación de primer grado
  """
    if A != 0:
        x = -B /A
        return x 
    else:
        print("No has ingresado una ecuacion de primer grado")

print(equation(4,5))