n = int(input(" Cuantos numeros enteros vas introducir?: "))

nums = []

for _ in range(n):
  sign = ""
  num = int(input())
  if num > 0:
    sign = "positivo"
  elif num == 0:
    sign = "cero"
  else:
    sign = "negativo"
  nums.append((num, sign))

print(nums)