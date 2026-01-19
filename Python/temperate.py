print("="*55)
print("  Bienvenue sur le convertisseur de la température : ")
print("="*55)
print("Voici les chiffres pour : ")
print("1 : Celsius ⮕ Fahrenheit")
print("2 : Fahrenheit ⮕ Celsius")
print("3 : Celsius ⮕ Kelvin")
print("4 : Kelvin ⮕ Celsius")
print("5 :  Fahrenheit ⮕ Kelvin")
print("6 :  Kelvin ⮕ Fahrenheit")

choix= input("Votre choix : ")
while choix not in ["1", "2", "3", "4", "5", "6"]:
    choix = input("Choix inavlide , Veuillez saisir le chiffre : ")
  
if choix == "1":
    nombre = float(input("Mettez votre nombre en Celsius : "))
    resultat = nombre*9/5 + 32
    print(f"Ça vous fera {resultat:.2f}°F")

elif choix == "2":
    nombre = float(input("Mettez votre nombre en Fahrenheit : "))
    resultat = (nombre - 32) * 5/9 
    print(f"Ça vous fera {resultat:.2f}°C")

elif choix == "3":
    nombre = float(input("Mettez votre nombre en Celsius : "))
    resultat = nombre + 273.15
    print(f"Ça vous fera {resultat:.2f}°K")

elif choix == "4":
    nombre = float(input("Mettez votre nombre en Kelvin : "))
    resultat = nombre - 273.15
    print(f"Ça vous fera {resultat:.2f}°C")

elif choix == "5":
    nombre = float(input("Mettez votre nombre en Fahrenheit : "))
    resultat = (nombre - 32) * 5/9 + 273.15
    print(f"Ça vous fera {resultat:.2f}°K")

elif choix == "6":
    nombre = float(input("Mettez votre nombre en Kelvin : "))
    resultat = (nombre - 273.15) * 9/5 + 32
    print(f"Ça vous fera {resultat:.2f}°F")