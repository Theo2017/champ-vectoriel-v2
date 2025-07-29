import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from utils import generer_champ

def afficher(type_champ):
    X, Y, U, V = generer_champ(type_champ)
    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, U, V)
    plt.title(f"Champ vectoriel : {type_champ}")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Champ vectoriel")

label = tk.Label(fenetre, text="Choisissez un champ :")
label.pack()

champ_choisi = tk.StringVar(value="rotation")
menu = ttk.Combobox(fenetre, textvariable=champ_choisi, values=["rotation", "radial", "spirale"])
menu.pack()

btn = tk.Button(fenetre, text="Afficher", command=lambda: afficher(champ_choisi.get()))
btn.pack()

fenetre.mainloop()
