from PIL import Image, ImageDraw
import numpy as np


def contour2(image):
    image = np.asarray(image, dtype=float)
    nb_lignes,nb_colonnes,z = image.shape
    
    # Le noyau :
    noyau_v = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    noyau_h = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
                        
    # Modification de l'image :
    image_sortie = np.copy(image)
    for ligne in range(1,nb_lignes-1):
        for col in range(1,nb_colonnes-1):
            # On calcule la somme 
            somme_v,somme_h = 0,0
            for l in range(3):
                for c in range(3):
                    somme_v += noyau_v[l,c]*image[ligne-1+l,col-1+c]
                    somme_h += noyau_h[l,c]*image[ligne-1+l,col-1+c]
            image_sortie[ligne,col] = (somme_v*somme_v+somme_h*somme_h)**0.5
    
    Image.fromarray(image_sortie.clip(0,255).astype("uint8")).save("test.bmp")

    # On sauvegarde les images pour pouvoir les afficher
    return Image.fromarray(image_sortie.clip(0,255).astype("uint8"))
# On charge l'image et on la transforme en tableau contenant les couleurs



