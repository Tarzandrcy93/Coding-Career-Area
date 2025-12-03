import time
print("Bienvenue sur le calculateur d'IMC (Indice de Masse Corporelle)")
time.sleep(1)
poids = float(input("Votre poids (kg) : "))
taille = float(input("Votre taille (cm) : "))
bmi = poids / (taille / 100) ** 2
time.sleep(1)
print("Calcul en cours...")
time.sleep(1)
print("Votre IMC est de", round(bmi, 2))
time.sleep(1)   
if bmi < 18:
	print("Vous êtes maigre 😊")
elif 18 <= bmi < 25:
    print("Vous êtes normal 🙂")
elif 25 <= bmi < 30:
    print("Vous êtes en surpoids 😐")
elif 30 <= bmi < 45:
    print("Vous êtes obèse 😧")
elif bmi >= 45:
    print("Vous êtes en obésité sévère 😨")
    