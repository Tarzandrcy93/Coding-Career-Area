import time

print("="*40)
print("  Bienvenue sur le compte à rebours : ")
print("="*40)

time.sleep(1)
input("Appuyez sur Entrée pour continuer...")
time.sleep(1)

def demander_nombre(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Nombre inconnu. Veuillez entrer un nombre en (secondes) :")

temps = demander_nombre("Entrez le nombre en (secondes): ")

for x in range(temps, 0, -1):
    seconde = x % 60
    minute = x // 60 % 60
    heure = x // 3600
    print(f"{heure:02d}:{minute:02d}:{seconde:02d}")
    time.sleep(1)
print("⏰ Temps écoulé ! ⏰")