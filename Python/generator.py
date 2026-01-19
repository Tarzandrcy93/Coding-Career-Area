import random

print("="*50)
print("  Bienvenue sur le generateur de Mot de Passe : ")
print("="*50)

Majuscle ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Miniscule ="abcdefghijklmnopqrstuvwxyz"
Chiffre ="0123456789"
Caractère = "?,.;/:§!"
Chars = Majuscle + Miniscule + Chiffre + Caractère 

password = ""
for x in range(10):
    password+= random.choice(Chars)
    if (x + 1) % 4 == 0 and x < 10:
       password += "-"


print(f"Ton mot de passe est : {password}")

