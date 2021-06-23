subjects = {"Math": [],
            "English": [],
            "History": [],
            "Science": [],
            "IT": []}

for key in subjects:
  print("===", key, "===")
  for i in range(1, 4):
    subjects[key].append(int(input("Nota trimestre {} ".format(i))))

print("\n Medias por asignatura:")
for key, val in subjects.items():
  print(key, ":", sum(val)/len(val))