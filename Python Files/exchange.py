print("Bienvenue dans le convertisseur de la monnaie")
print("Mettez les chiffres pour : ")
print("1 : Sterling ⮕ Euro")
print("2 : Euro ⮕ Sterling")
print("3 : Euro ⮕ Dollar Américain")
print("4 : Dollar Américain ⮕ Euro")
print("5 : Sterling ⮕ Dollar Américain")
print("6 : Dollar Américain ⮕ Sterling")
print("")

Euro = 1.15      # 1 £ = 1.15 €
Sterling = 0.87  # 1 € = 0.87 £
Dollar_américain = 1.17 # 1€ = 1.17

choix= input("Votre choix : ")
while choix not in ["1", "2"]:
    choix = input("Choix inavlide , Veuillez rentrer le chiffre : ")
  
if choix == "1":
    montant = float(input("Mettez votre nombre en Sterling : "))
    resultat = montant * Euro
    print(f"Ça vous fera {resultat:.2f} €")

elif choix == "2":
    montant = float(input("Mettez votre nombre en Euro : "))
    resultat = montant * Sterling
    print(f"Ça vous fera {resultat:.2f} £")


