from cv2 import imwrite
from random import randint
import numpy as np

# choix de la taille de l'image générée
# doit remplir la condition : h = 2^n + 1
h = 513

# crée une image
image = np.zeros((h, h, 3), np.uint8)

def fonction(image):
    # initialisation des coins
    # génération noire et blanche
    image[0  , 0  ] = randint(0, 255)
    image[0  , h-1] = randint(0, 255)
    image[h-1, h-1] = randint(0, 255)
    image[h-1, 0  ] = randint(0, 255)

    # génération colorée ( inutilisable pour la traiterImage.py )
    #image[0  , 0  ] = [randint(0, 255), randint(0, 255), randint(0, 255)]
    #image[0  , h-1] = [randint(0, 255), randint(0, 255), randint(0, 255)]
    #image[h-1, h-1] = [randint(0, 255), randint(0, 255), randint(0, 255)]
    #image[h-1, 0  ] = [randint(0, 255), randint(0, 255), randint(0, 255)]

    i = h-1

    while i > 1:
        i2 = i//2

        # début phase diamant
        for x in range(i2, h, i):
            for y in range(i2, h, i):
                moyenne = [
                    int(int(image[x - i2, y - i2][0]) + int(image[x - i2, y + i2][0]) + int(image[x + i2, y + i2][0]) + int(image[x + i2, y - i2][0]))/4,
                    int(int(image[x - i2, y - i2][1]) + int(image[x - i2, y + i2][1]) + int(image[x + i2, y + i2][1]) + int(image[x + i2, y - i2][1]))/4,
                    int(int(image[x - i2, y - i2][2]) + int(image[x - i2, y + i2][2]) + int(image[x + i2, y + i2][2]) + int(image[x + i2, y - i2][2]))/4
                ]

                hasard = randint(-int(i2/2), int(i2/2))

                image[x, y] = [
                    moyenne[0] + hasard,
                    moyenne[1] + hasard,
                    moyenne[2] + hasard
                ]

        decalage = 0

        # début phase carré
        for x in range(0, h, i2):
            if decalage == 0:
                decalage = i2
            else:
                decalage = 0

            for y in range(decalage, h, i):
                somme = [0, 0, 0]
                n = 0

                if x >= i2:
                    somme[0] += image[x - i2, y][0]
                    somme[1] += image[x - i2, y][1]
                    somme[2] += image[x - i2, y][2]

                    n += 1

                if x + i2 < h:
                    somme[0] += image[x + i2, y][0]
                    somme[1] += image[x + i2, y][1]
                    somme[2] += image[x + i2, y][2]

                    n += 1

                if y >= i2:
                    somme[0] += image[x, y - i2][0]
                    somme[1] += image[x, y - i2][1]
                    somme[2] += image[x, y - i2][2]

                    n += 1

                if y + i2 < h:
                    somme[0] += image[x, y + i2][0]
                    somme[1] += image[x, y + i2][1]
                    somme[2] += image[x, y + i2][2]

                    n += 1

                hasard = randint(-int(i2/2), int(i2/2))

                image[x, y] = [somme[0] / n + hasard, somme[1] / n + hasard, somme[2] / n + hasard]

        i = i2

for i in range(4):
    fonction(image)

    name = "basesGenerees/base" + str(i) + ".png"

    imwrite(name, image)