from cv2 import imread, imwrite
import numpy as np
from random import randint

# génération d'une image via genererImage.py
#exec(open("./genererBase.py").read())

image = imread("bases_noires_et_blanches/base0.png")

h = image.shape[0]

map = np.zeros((h, h, 3), np.uint8)

def traiterImage(type):
    if type == "desert":
        for x in range(h):
            for y in range(h):
                if   image[x, y][0] > 160: map[x, y] = [ 96,  96,   0] # eau profonde
                elif image[x, y][0] > 130: map[x, y] = [127, 127,   0] # eau
                elif image[x, y][0] > 110: map[x, y] = [  0, 255, 255] # sable
                elif image[x, y][0] >  80: map[x, y] = [  0, 198, 198] # sol
                elif image[x, y][0] >  40: map[x, y] = [  0,  96,  96] # roche
                elif image[x, y][0] >  20: map[x, y] = [  0,  48,  64] # montagne
                else                     : map[x, y] = [  0,  32,  64] # sommets
    
    elif type == "glace":
        for x in range(h):
            for y in range(h):
                if   image[x, y][0] > 160: map[x, y] = [127,   0,   0] # eau profonde
                elif image[x, y][0] > 130: map[x, y] = [255,   0,   0] # eau
                elif image[x, y][0] > 110: map[x, y] = [255, 150, 150] # bord d'eau
                elif image[x, y][0] >  80: map[x, y] = [255, 200, 200] # sol
                elif image[x, y][0] >  40: map[x, y] = [190, 190, 190] # plutot haut
                elif image[x, y][0] >  20: map[x, y] = [220, 220, 220] # haut
                else                     : map[x, y] = [255, 255, 255] # très haut

    elif type == "enfer":
        for x in range(h):
            for y in range(h):
                if   image[x, y][0] > 160: map[x, y] = [ 32,  32, 255] # lave profonde
                elif image[x, y][0] > 130: map[x, y] = [ 64,  64, 255] # lave
                elif image[x, y][0] > 125: map[x, y] = [ 32,  32,  32] # sable noir
                elif image[x, y][0] >  90: map[x, y] = [  0,  32,  64] # sol
                elif image[x, y][0] >  55: map[x, y] = [  0,  16,  32] # forêt
                elif image[x, y][0] >  20: map[x, y] = [ 16,  16,  16] # montagne
                else                     : map[x, y] = [  0,   0,   0] # sommets
    
    else:
        for x in range(h):
            for y in range(h):
                if   image[x, y][0] > 160: map[x, y] = [127,   0,   0] # eau profonde
                elif image[x, y][0] > 130: map[x, y] = [255,   0,   0] # eau
                elif image[x, y][0] > 125: map[x, y] = [  0, 255, 255] # sable
                elif image[x, y][0] >  90: map[x, y] = [  0, 255,   0] # herbe
                elif image[x, y][0] >  55: map[x, y] = [  0, 127,   0] # forêt
                elif image[x, y][0] >  20: map[x, y] = [ 63,  63,  63] # montagne
                else                     : map[x, y] = [255, 255, 255] # sommets

tabTypes = ["desert", "glace", "enfer", "autre"]

for i in range(len(tabTypes)):
    traiterImage(tabTypes[i])

    name = "cartes/" + tabTypes[i] + ".png"

    imwrite(name, map)