import tkinter as tk
import pyautogui

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Compteur")

# Création d'un compteur
compteur = 0

# Recupère le compteur dans le fichier txt
with open('totalMorts.txt', 'r') as f:
    compteur = f.read()

# Configurer la taille de la fenêtre principale
fenetre.geometry("200x100-30+40")

# Configurer la fenêtre pour qu'elle reste toujours au-dessus des autres fenêtres
fenetre.attributes("-topmost", True)

# Configurer la couleur de fond de la fenêtre
fenetre.configure(bg="black")

# Chemin vers l'image à détecter
chemin_image = "./img/VousAvezPeri.png.PNG"

# Création de la fonction pour incrémenter le compteur
def incrementer():
    global compteur

    # Détecter l'apparition de l'image à l'écran
    image = pyautogui.locateOnScreen(chemin_image) #, confidence=0.5, region=(250,650,1400,700)
    print(pyautogui.locateOnScreen(chemin_image))

    # Si l'image est détectée, incrémenter le compteur
    if image:
        compteur = int(compteur)
        compteur += 1
        label.configure(text="Tu es mort {} fois".format(compteur), fg="red")
        with open('totalMorts.txt', 'w') as f:
            f.write(str(compteur))
    fenetre.after(1000, incrementer)

def remettre_a_zero():
    with open('totalMorts.txt', 'w') as f:
        f.write('0')
        label.configure(text="Tu es mort 0 fois")
        global compteur
        compteur = 0

# Création d'un label pour afficher le compteur
label = tk.Label(fenetre, text="Tu es mort {} fois".format(compteur), bg="black", fg="red", font=("Helvetica", 16))
label.pack(side="top",expand=True, fill="both")

# Création d'un bouton pour remettre le compteur à zéro
bouton_reset = tk.Button(fenetre, text="Remettre à zéro", command=remettre_a_zero, bg="grey")
bouton_reset.pack(side="bottom", fill="x")

# Exécution de la fonction d'incrémentation toutes les secondes
fenetre.after(1000, incrementer)

# Affichage de la fenêtre
fenetre.mainloop()