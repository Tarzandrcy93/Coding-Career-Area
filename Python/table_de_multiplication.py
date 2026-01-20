def demander_nombre(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier : ")

choix = demander_nombre("Entrez un nombre entier : ")


for facteur in range (1, 13):
    resultat = choix * facteur
    print (f"{choix} x {facteur} = {resultat}")
