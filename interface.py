import matplotlib.pyplot as plt
from utils import generer_champ

def afficher_champ(type_champ):
    X, Y, U, V = generer_champ(type_champ)
    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, U, V)
    plt.title(f"Champ vectoriel : {type_champ}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    for t in ["rotation", "radial", "spirale"]:
        afficher_champ(t)
