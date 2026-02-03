import pyttsx3

print("="*60)
print("   Bienvenue dans le conversion d'audio par un texte !!!")
print("="*60)

engine = pyttsx3.init()
texte = input("Entrez le texte à convertir en audio : ")

engine.save_to_file(text=texte, filename='audio.mp3')
engine.runAndWait()

print("Conversion terminée ! Le fichier audio 'audio.mp3' a été créé.")