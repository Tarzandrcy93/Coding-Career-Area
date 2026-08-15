import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print("="*38)
print("    Bienvenue sur le calendrier :")
print("="*38)

def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

année = int(demander_nombre("Entrez une année : "))

mois = int(demander_nombre("Entrez un mois : "))

print(calendar.month(année, mois))