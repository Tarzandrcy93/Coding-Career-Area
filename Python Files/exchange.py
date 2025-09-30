print("Bienvenue dans le convertisseur de la monnaie")
print("Voici les chiffres pour : ")
print("1 : Sterling ⮕ Euro")
print("2 : Euro ⮕ Sterling")
print("3 : Euro ⮕ Dollar Américain")
print("4 : Dollar Américain ⮕ Euro")
print("5 : Sterling ⮕ Dollar Américain")
print("6 : Dollar Américain ⮕ Sterling")

Euro = 1.14      
Sterling = 0.87  
Dollar_américain = 1.17 
Euro_d= 0.85 
dollar_s= 1.34 
Sterling_d= 0.74


choix= input("Votre choix : ")
while choix not in ["1", "2", "3", "4", "5", "6"]:
    choix = input("Choix inavlide , Veuillez saisir le chiffre : ")
  
if choix == "1":
    montant = float(input("Entrez votre nombre en Sterling : "))
    resultat = montant * Euro
    print(f"Ça vous fera {resultat:.2f} €")

elif choix == "2":
    montant = float(input("Entrez votre nombre en Euro : "))
    resultat = montant * Sterling
    print(f"Ça vous fera {resultat:.2f} £")

elif choix == "3":
    montant = float(input("Entrez votre nombre en Euro : "))
    resultat = montant * Dollar_américain
    print(f"Ça vous fera {resultat:.2f} $")
    
elif choix == "4":
    montant = float(input("Entrez votre nombre en Dollar Américain : "))
    resultat = montant * Euro_d
    print(f"Ça vous fera {resultat:.2f} €")
    
elif choix == "5":
    montant = float(input("Entrez votre nombre en Sterling: "))
    resultat = montant * dollar_s
    print(f"Ça vous fera {resultat:.2f} $")
    
elif choix == "6":
    montant = float(input("Entrez votre nombre en Dollar Américain : "))
    resultat = montant * Sterling_d
    print(f"Ça vous fera {resultat:.2f} £")

