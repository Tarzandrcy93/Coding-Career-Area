import time

print("="*60)
print("  Bienvenue sur le calculateur de votre moyenne générale ")
print("="*60)


notes = []

while True:
    valeur = input("Entrez une moyenne (ou FIN pour terminer) : ")

    if valeur.upper() == "FIN":
        break

    try:
        note = float(valeur)
        notes.append(note)
    except ValueError:
        print("Entrée invalide, veuillez entrer un nombre.")

time.sleep(1)
print("Calcul de votre moyenne générale en cours...")
time.sleep(1)

if len(notes) == 0:
    print("Aucune note entrée.")
else:
    mg = sum(notes) / len(notes)
    print(f"Votre moyenne générale est de {mg:.2f} / 20 👌👌👌")