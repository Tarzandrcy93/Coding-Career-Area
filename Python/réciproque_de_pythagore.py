print("Voici la réproque de Pythagore : Si A² + B² = C², alors le triangle est rectangle.")
     
a = float(input("Entrez la longueur du côté A : "))
b = float(input("Entrez la longueur du côté B : "))
c = float(input("Entrez la longueur du côté C (hypoténuse) : "))

if a**2 + b**2 == c**2:
    print("Le triangle est rectangle.")         
else:
    print("Le triangle n'est pas rectangle.")