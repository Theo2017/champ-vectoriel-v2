from utils import generer_champ

def test_champs():
    types = ["rotation", "radial", "spirale"]
    for t in types:
        X, Y, U, V = generer_champ(t)
        print(f"{t} → Champ généré de taille : {X.shape}")

if __name__ == "__main__":
    test_champs()
