n = int(input("Cuantos puntos vas a introducir?>: "))
points=[]
for i in range(n):
  x = float(input("Indica la coordenada x: "))
  y = float(input("Indica la coordenada y: "))

  if x >= 0 and y >=0:
    quadrant = "I"
  if x <= 0 and y >=0:
    quadrant = "II"
  if x <= 0 and y <=0:
    quadrant = "III"
  if x >= 0 and y <=0:
    quadrant = "IV"
  if x == 0 and y ==0:
    quadrant = "center"
  points.append((x, y, quadrant))

for point in points:
  x,y,quadrant = point
  print("El punto {}, {} perteneces al cuadrante {}".format(x, y , quadrant))
