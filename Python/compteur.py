import time

print("="*40)
print(" Bienvenue dans le compteur de nombre : ")
print("="*40)


def demander_nombre(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


nombre = demander_nombre("Entrez un nombre entier : ")
time.sleep(1)
print("Chargement en cours...")
time.sleep(1)

for i in range (1, nombre + 1):
    print(i)
    
    