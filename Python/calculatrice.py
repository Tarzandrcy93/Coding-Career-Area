print("="*40)
print("  Bienvenue sur la calculatrice STC : ")
print("="*40)

def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


calcul = input("Entrez votre signe d'operatation (+, -, *, /) : ")
while calcul not in ["+", "-", "*", "/"]:
    calcul = input("Signe non recconue . Veuiilez entrez votre signe d'operatation (+, -, *, /) : ")
    
num1 = demander_nombre("Entrez le premier nombre : ")
num2 = demander_nombre("Entrez le deuxieme nombre : ")


if calcul == "+":
    resultat = num1 + num2
    print(f"Le résultat est {resultat}")
elif calcul == "-":
    resultat = num1 - num2
    print(f"Le résultat est {resultat}")
elif calcul == "*":
    resultat = num1 * num2
    print(f"Le résultat est {resultat}")            
elif calcul == "/":
    if num2 != 0:
        resultat = num1 / num2
        print(f"Le résultat est {resultat}")
    else:
        print("Erreur : Division par zéro impossible.")