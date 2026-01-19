print("="*60)
print("    Bienvenue dans le système d'authentification de STC ")
print("="*60) 

connected = False
mdp_corect = "487382"

while not connected:
    saise=input("Veuillez entrer le mot de passe : ")
    if saise == mdp_corect:
        connected = True
        print("Connexion réussie !")
    else:
        print("Mot de passe incorrect. Veuillez réessayer.")
