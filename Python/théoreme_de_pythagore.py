print("Bienvenue dans la théoreme de Pythagore ou la réciproque de Pythagore")
Choix = input("Tapez 1 = le théorème de Pythagore ou 2 = la réciproque de Pythagore : ")

if Choix == "1":  
    print("Voici le théorème de Pythagore : A² + B² = C²")
    a = float(input("Entrez la longueur du côté A : "))
    b = float(input("Entrez la longueur du côté B : "))
    c = (a**2 + b**2)**0.5
    print(f"La longueur de l'hypoténuse C est {c}")


elif Choix == "2":
    print("Voici la réproque de Pythagore : Si A² + B² = C², alors le triangle est rectangle.")
     
    a = float(input("Entrez la longueur du côté A : "))
    b = float(input("Entrez la longueur du côté B : "))
    c = float(input("Entrez la longueur du côté C (hypoténuse) : "))

    if a**2 + b**2 == c**2:
        print("Le triangle est rectangle.")  
    else:
        print("Le triangle n'est pas rectangle.")