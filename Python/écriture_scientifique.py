print("="*55)
print("  Bienvenue sur le programme d'écriture scientifique :")
print("="*55)

def demander_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

nombre  = demander_nombre("Entrez un nombre : ")

exposant = 0
if nombre != 0:
    while abs(nombre) >= 10:
        nombre /= 10
        exposant += 1
    while abs(nombre) < 1:
        nombre *= 10
        exposant -= 1   
print(f"L'écriture scientifique est {nombre} x 10^{exposant}")