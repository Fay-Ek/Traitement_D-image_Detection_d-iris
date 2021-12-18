
from PIL import Image, ImageDraw
import numpy as np
import statistics

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("b.bmp"))
nb_lignes,nb_colonnes= image.shape

# Le noyau :
noyau = np.zeros([3, 3])
noyau1 = np.zeros([9,1])

# Modification de l'image :
image_sortie = np.copy(image)
for ligne in range(1,nb_lignes-1):
    for col in range(1,nb_colonnes-1):
        # On calcule la somme 
        somme = 0
        o=0
        for l in range(3):
            for c in range(3):
                noyau1[o]=image[ligne-1+l,col-1+c] 
                o=o+1
        image_sortie[ligne,col] = statistics.median(noyau1)


# On sauvegarde les images pour pouvoir les afficher
#Image.fromarray(image).save("lissage1_entree.png")
Image.fromarray(image_sortie).save("median.png")


