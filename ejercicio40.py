def countletter(s,letter):
    s = s.lower()
    con = s.count(letter)
    return con

s = input("Introduce una frase:")
letter = input("iNTRODUCE UNA LETRA")

print(countletter(s,letter))