## Ano bisiesto 
year = int(input("Year: "))

if year % 4 == 0:
    if year % 100:
       if year % 400:
           print("This year {} is bisiesto".format(year))  
       else: print("This year {} is not bisiesto".format(year))
    else: 
         print("This year {} is bisiesto".format(year))  
else: 
    print("This year {} is not bisiesto ".format(year))