print("Bienvenue dans le convertisseur de Sterling ⮕ Euro ou Euro ⮕ Sterling")
print("Mettez 1 ⮕ Euro ou 2 ⮕ Sterling ")

Euro = 1.15      # 1 £ = 1.15 €
Sterling = 0.87  # 1 € = 0.87 £

choix = input("Votre choix : ")

if choix == "1":
    montant = float(input("Mettez votre nombre en Sterling : "))
    resultat = montant * Euro
    print(f"Ça vous fera {resultat:.2f} €")

elif choix == "2":
    montant = float(input("Mettez votre nombre en Euro : "))
    resultat = montant * Sterling
    print(f"Ça vous fera {resultat:.2f} £")

else:
 print("Choix invalide, veuillez entrer 1 ou 2.")
