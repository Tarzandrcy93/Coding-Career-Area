import json
import os
import random

FICHIER_COMPTES = "index.json"

def charger_comptes():
    if os.path.exists(FICHIER_COMPTES):
        with open(FICHIER_COMPTES, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def sauvegarder_comptes(comptes):
    with open(FICHIER_COMPTES, "w") as f:
        json.dump(comptes, f, indent=4)

def creer_compte(comptes):
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    age = input("Âge : ")
    while not age.isdigit() or int(age) <= 0:
        age = input("Veuillez entrer un âge valide : ")
    identifiant = input("Identifiant : ")
    email = input("E-mail : ")
    if email in comptes:
        print("E-mail déjà utilisé.")
        return
    mot_de_passe = input("Mot de passe : ")
    pin = str(random.randint(0, 999999)).zfill(6)  # Générer un code PIN à 6 chiffres
    comptes[email] = {
        "prenom": prenom,
        "nom": nom,
        "age": int(age),
        "identifiant": identifiant,
        "email": email,
        "mot_de_passe": mot_de_passe,
        "pin": pin
    }
    sauvegarder_comptes(comptes)
    print("Compte créé avec succès !")
    print("Vérification du compte !")
    pin_saisi = input("Veuillez saisir le code PIN : ")
    while pin_saisi != pin:
        pin_saisi = input("PIN incorrect. Veuillez réessayer : ")
    print("PIN accepté !")
    print("Bienvenue sur votre compte STC !")

def connexion(comptes):
    email = input('Entrer votre e-mail : ')
    while email not in comptes:
        email = input('E-mail non reconnu. Veuillez entrer votre e-mail à nouveau : ')
    print('E-mail accepté !')
    password = input('Entrer votre mot de passe : ')
    while password != comptes[email]["mot_de_passe"]:
        password = input('Mot de passe incorrect. Veuillez entrer votre mot de passe à nouveau : ')
    print('Mot de passe accepté !')
    print(f'Bienvenue {comptes[email]["identifiant"]}  sur votre compte !')  

# --- Programme principal ---
print('Bienvenue sur le Projet STC')
comptes = charger_comptes()

choix = input("(Tapez 1 = s'inscrire) ou (Tapez 2 = se connecter) : ")
if choix == "1":
    creer_compte(comptes)
elif choix == "2":
    connexion(comptes)
else:
    print("Choix invalide.")
while True:
    choix = input("(Tapez 1 = s'inscrire) ou (Tapez 2 = se connecter) : ")
    if choix == "1":
        creer_compte(comptes)
    elif choix == "2":
        connexion(comptes)
    else:
        print("Choix invalide.")