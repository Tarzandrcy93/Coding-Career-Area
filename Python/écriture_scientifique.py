print("Bienvenue sur le programme d'écriture scientifique :")

nombre  = float(input("Entrez un nombre : "))
exposant = 0
if nombre != 0:
    while abs(nombre) >= 10:
        nombre /= 10
        exposant += 1
    while abs(nombre) < 1:
        nombre *= 10
        exposant -= 1   
print(f"L'écriture scientifique est {nombre} x 10^{exposant}")