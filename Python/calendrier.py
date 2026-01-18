import calendar

print("="*38)
print("    Bienvenue sur le calendrier :")
print("="*38)
année = int(input("Entrez une année : "))
mois =  int(input("Entrez un mois : "))

print(calendar.month(année, mois))