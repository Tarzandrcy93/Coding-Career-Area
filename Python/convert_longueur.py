import time

print("Bienvenue dans le convertisseur de longueurs :")
time.sleep(1)
print("Voici les unités de longueur disponibles : mm , cm , dm , m , dam , hm , km")
time.sleep(1)

choix = input("Choisissez l'unité de longueur : ")
unité_de_longueur = input("A quelle unité de longueur voulez-vous convertir : ")

valeur = float(input("Entrez le nombre de l'unité de longueur: "))

if choix == "mm":
    if unité_de_longueur == "cm":
        résultat = valeur / 10
    elif unité_de_longueur == "dm":
        résultat = valeur / 100
    elif unité_de_longueur == "m":
        résultat = valeur / 1000
    elif unité_de_longueur == "dam":
        résultat = valeur / 10000
    elif unité_de_longueur == "hm":
        résultat = valeur / 100000
    elif unité_de_longueur == "km":
        résultat = valeur / 1000000
    else:
        print("Unité de longueur non reconnue.")

elif choix == "cm":
    if unité_de_longueur == "mm":
        résultat = valeur * 10
    elif unité_de_longueur == "dm":
        résultat = valeur / 10
    elif unité_de_longueur == "m":
        résultat = valeur / 100
    elif unité_de_longueur == "dam":
        résultat = valeur / 1000
    elif unité_de_longueur == "hm":
        résultat = valeur / 10000
    elif unité_de_longueur == "km":
        résultat = valeur / 100000
    else:
        print("Unité de longueur non reconnue.")

elif choix == "dm":
    if unité_de_longueur == "mm":
        résultat = valeur * 100
    elif unité_de_longueur == "cm":
        résultat = valeur * 10
    elif unité_de_longueur == "m":
        résultat = valeur / 10
    elif unité_de_longueur == "dam":
        résultat = valeur / 100
    elif unité_de_longueur == "hm":
        résultat = valeur / 1000
    elif unité_de_longueur == "km":
        résultat = valeur / 10000
    else:
        print("Unité de longueur non reconnue.")
        
elif choix == "m":
    if unité_de_longueur == "mm":
        résultat = valeur * 1000
    elif unité_de_longueur == "cm":
        résultat = valeur * 100
    elif unité_de_longueur == "dm":
        résultat = valeur * 10
    elif unité_de_longueur == "dam":
        résultat = valeur / 10
    elif unité_de_longueur == "hm":
        résultat = valeur / 100
    elif unité_de_longueur == "km":
        résultat = valeur / 1000
    else:
        print("Unité de longueur non reconnue.")

elif choix == "dam":
    if unité_de_longueur == "mm":
        résultat = valeur * 10000
    elif unité_de_longueur == "cm":
        résultat = valeur * 1000
    elif unité_de_longueur == "dm":
        résultat = valeur * 100
    elif unité_de_longueur == "m":
        résultat = valeur * 10
    elif unité_de_longueur == "hm":
        résultat = valeur / 10
    elif unité_de_longueur == "km":
        résultat = valeur / 1000
    else:
        print("Unité de longueur non reconnue.")

elif choix == "hm":
    if unité_de_longueur == "mm":
        résultat = valeur * 100000
    elif unité_de_longueur == "cm":
        résultat = valeur * 10000
    elif unité_de_longueur == "dm":
        résultat = valeur * 1000
    elif unité_de_longueur == "m":
        résultat = valeur * 100
    elif unité_de_longueur == "km":
        résultat = valeur / 10
    else:
        print("Unité de longueur non reconnue.")

elif choix == "km":
    if unité_de_longueur == "mm":
        résultat = valeur * 1000000
    elif unité_de_longueur == "cm":
        résultat = valeur * 100000
    elif unité_de_longueur == "dm":
        résultat = valeur * 10000
    elif unité_de_longueur == "m":
        résultat = valeur * 1000
    elif unité_de_longueur == "hm":
        résultat = valeur / 100
    else:
        print("Unité de longueur non reconnue.")

print("le résultat est de ", résultat)