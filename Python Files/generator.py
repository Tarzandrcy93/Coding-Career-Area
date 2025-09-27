import random

print("Bienvenue sur le generateur de Mot de Passe")

Majuscle ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Miniscule ="abcdefghijklmnopqrstuvwxyz"
Chiffre ="0123456789"
Caractère = "?,.;/:§!"
Chars = Majuscle + Miniscule + Chiffre + Caractère 

print("Your password is : ")
password = ""
for x in range(10):
    password+= random.choice(Chars)
    if (x + 1) % 4 == 0 and x < 10:
       password += "-"

print(password)