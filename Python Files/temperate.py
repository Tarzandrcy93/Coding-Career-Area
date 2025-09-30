print("Bienvenue sur le convertisseur des Celsius ou Fahrenheit")
print("Voici les chiffres pour : ")
print("1 : Sterling ⮕ Euro")
print("2 : Euro ⮕ Sterling")
print("3 : Euro ⮕ Dollar Américain")
print("4 : Dollar Américain ⮕ Euro")
print("5 : Sterling ⮕ Dollar Américain")
print("6 : Dollar Américain ⮕ Sterling")

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

