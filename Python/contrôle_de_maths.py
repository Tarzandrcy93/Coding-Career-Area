import time

bonnes_reponses = 0
print("Bienvenue sur le contrôle de Maths")
time.sleep(0.5)
print("Le contrôle est noté sur 10")
time.sleep(0.5)
input("Appuyez sur Entrée pour commencer")
time.sleep
un = input("1) 4 + 5 = ")
if un == "9":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
deux = input("2) 10 - 6 = ")
if deux =="4":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
trois = input("3) 8 X 2 = ")
if trois =="16":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")

quatre = input("4) 24 ÷ 3 = ")
if quatre =="8":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
cinq = input("5) 7 + 7 - 7 x 7 ÷ 7 = ")
if cinq =="7":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")

six = input("6) 9^2 = ")
if six =="81":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
sept = input("7) √121 = ")
if sept =="11":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
huit= input("8) x + 12 = 15 : x = ")
if huit =="3":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
neuf = input("9) x X 2 + 10 = 30 : x = ")
if neuf =="10":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
    
dix = input("10) 2x + 32 = 4x - 8 : x = ")
if dix =="20":
    print("Bonne réponse !")
    bonnes_reponses += 1
else :
    print("Mauvaise réponse !")
time.sleep(2)
print("En cours de la correction %")
time.sleep(2)

print(f"Bravo !!! Tu as obtenu {bonnes_reponses} bonnes réponses .")

if bonnes_reponses >= 5:
    print("Tu as reussi le contrôle 👌😁 !")
else :
    print("Tu as raté le contrôle 😡🫢 !")