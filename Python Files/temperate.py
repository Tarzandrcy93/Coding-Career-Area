print("Bienvenue sur le convertisseur des Celsius ou Fahrenheit")
print("Tapez 1 ⮕ Fahrenheit ou 2 ⮕ Celsius :")

choix = input("Votre choix : ")

if choix == "1":
    nombre = float(input("Mettez votre nombre en Celsius : "))
    resultat = nombre*9/5 + 32
    print(f"Ça vous fera {resultat:.2f}°F")

elif choix == "2":
    nombre = float(input("Mettez votre nombre en Fahrenheit : "))
    resultat = (nombre - 32) * 5/9 
    print(f"Ça vous fera {resultat:.2f}°C")

else:
 print("Choix invalide, veuillez entrer 1 ou 2.")
