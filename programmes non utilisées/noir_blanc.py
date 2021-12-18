from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("contour111.bmp"),dtype = float)
nb_lignes,nb_colonnes = image.shape

           
# Modification de l'image :
image_sortie = np.copy(image)
size=nb_lignes*nb_colonnes
s=0
for ligne in range(1,nb_lignes-1):
    for col in range(1,nb_colonnes-1):
        # On calcule la somme 
        if image_sortie[ligne,col] <100:
            image_sortie[ligne,col] = 0
            s=s+1
        else:
            image_sortie[ligne,col] = 255


# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image_sortie.clip(0,255).astype("uint8")).save("noir3.bmp")

