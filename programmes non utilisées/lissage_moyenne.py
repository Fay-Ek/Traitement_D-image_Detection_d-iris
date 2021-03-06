
from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("histo4.bmp"))
nb_lignes,nb_colonnes= image.shape

# Le noyau :
noyau = np.array([[1/9, 1/9, 1/9],
                  [1/9,1/9, 1/9],
                  [1/9, 1/9, 1/9 ]])

# Modification de l'image :
image_sortie = np.copy(image)
for ligne in range(1,nb_lignes-1):
    for col in range(1,nb_colonnes-1):
        # On calcule la somme 
        somme = 0
        for l in range(3):
            for c in range(3):
                somme += noyau[l,c]*image[ligne-1+l,col-1+c] 
        image_sortie[ligne,col] = somme


# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image_sortie).save("lissage4.bmp")















