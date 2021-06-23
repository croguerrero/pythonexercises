subjects = ["Mates","Lengua", "Historia", "Informatica","Musica"]
grades = []

print(subjects)
s = input("Indica la asignatura: ")

while s in subjects:
  grade = int(input("Introduce la nota 1 a 10:"))
  grades.append((s,grade))
  s = input("Indica la asignatura: ")

mens = {
    "Mates":[],
    "Lengua":[],
    "Historia":[],
    "Informatica":[],
    "Musica":[]
}
for item in grades:
    mens[item[0]].append(item[1])

print("======Notas Medias=======")

for key, val in mens.items():
    print("La nota media {} es {}".format(key, "Desconocida" if len(val) ==0 else sum(val)/len(val) ))