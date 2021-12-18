# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:57:27 2021

@author: Lenovo
"""
from PIL import Image
import numpy as np

def noir_et_blanc():
    img = Image.open("EnrollementBDD/001_1_1.bmp")
    tab = np.array(img)
    nb_lignes,nb_colonnes = tab.shape
    for i in range(1,nb_lignes-1):
            for j in range(1,nb_colonnes-1):
                if(tab[i,j]<100):
                    tab[i,j]=0
                else:    
                    tab[i,j]=255
        
    return Image.fromarray(tab)