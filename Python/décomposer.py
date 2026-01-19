import time

print("="*70)
print("  Voici sur les décompositions en facteurs premiers des nombres :")
print("="*70)

time.sleep(1)
input("Appuyez sur Entrée pour continuer...")
time.sleep(1)

while True:
    try:
        nombre = int(input("Choisissez un nombre entier : "))
        break
    except ValueError:
        print("⚠️ Ce n'est pas un entier valide. Réessaie.")

def facteurs_premiers(n):
    facteurs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            facteurs.append(d)
            n //= d
        d += 1
    if n > 1:
        facteurs.append(n)
    return facteurs

# Formatage du résultat
facteurs = facteurs_premiers(nombre)
expression = " x ".join(str(f) for f in facteurs)
print(f"{nombre} = {expression}")