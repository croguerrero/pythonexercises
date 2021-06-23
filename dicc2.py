dicc = {"username": "msf",
        "name": "María",
        "age": 22,
        "city": "Palma de Mallorca"}

for key in dicc:
  print(key, ":", dicc[key])

dicc.items()

for item in dicc.items():
    print(item)

#### estructura de datos en datos diferentes

for key, value in dicc.items():
    print(key, ":", value)

###########combinacion de diccionarios y lista
dicc_1 = {"name": "Elisa",
        "age": 30,
        "gender": "female",
        "ID": [4, 4, 2, 1, 5, 6, 7, 2, "L"],
        "user&password": {
            "username": "eli88",
            "password": "1234catsareawesome"
            }
          }
dicc_2 = {"name": "Henry",
        "age": 27,
        "gender": "male",
        "ID": [1, 1, 0, 1, 3, 8, 6, 9, "A"],
        "user&password": {
            "username": "superhenry",
            "password": "1432superme"
            }
          }
lista = [dicc_1, dicc_2]

for item in lista:
    print(item)