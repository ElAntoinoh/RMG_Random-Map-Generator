import numpy as np
import sys
from random import randint
from cv2 import imwrite

# Création de l'image de base
image = np.zeros((16, 16, 3), np.uint8)

# Récupération de la couleur passée en paramètres
r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

# Variable désignant la variation maximale de la couleur de base 
rng = 16


def genererCase():
    for x in range(16):
        for y in range(16):
            newColor = [r, g, b]

            for i in range(3):
                if  (newColor[i]       < rng): newColor[i] += randint(             - newColor[i] , rng + newColor[i])
                elif(newColor[i] + rng > 255): newColor[i] += randint(- rng - (255 - newColor[i]), 255 - newColor[i])
                else                         : newColor[i] += randint(- rng                      , rng              )
            
            image[x, y] = [newColor[0], newColor[1], newColor[2]]


for i in range(4):
    genererCase()

    name = "cases/case" + str(i) + ".png"

    imwrite(name, image)