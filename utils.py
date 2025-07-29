import numpy as np

def generer_champ(type_champ, xlim=(-5, 5), ylim=(-5, 5), resolution=51):
    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(x, y)

    if type_champ == "rotation":
        U = -Y
        V = X
    elif type_champ == "radial":
        U = X
        V = Y
    elif type_champ == "spirale":
        U = -Y + X
        V = X + Y
    else:
        raise ValueError(f"Type de champ non reconnu : {type_champ}")

    return X, Y, U, V
