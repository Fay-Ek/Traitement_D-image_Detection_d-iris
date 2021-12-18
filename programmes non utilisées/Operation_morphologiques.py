# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:41:09 2021

@author: Lenovo
"""

from PIL import Image
import numpy as np








def filtre_colonne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre colonne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 0 
            if(tab[i-1,j] == noyau[0,1]):
                s=1
            if(tab[i,j] == noyau[1,1]):
                s=1
            if(tab[i+1,j] == noyau[2,1]):
                s=1
    
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
                
    return tab2
       




def filtre_ligne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre ligne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 0 
            if(tab[i,j-1] == noyau[1,0]):
                s=1
            if(tab[i,j] == noyau[1,1]):
                s=1
            if(tab[i,j+1] == noyau[1,2]):
                s=1
    
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
    
    return tab2    
    

        
def filtre_ligne_colonne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre ligne/colonne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 0 
            if(tab[i-1,j] == noyau[0,1]):
                s=1
            if(tab[i,j] == noyau[1,1]):
                s=1
            if(tab[i+1,j] == noyau[2,1]):
                s=1
            if(tab[i,j-1] == noyau[1,0]):
                s=1
            if(tab[i,j] == noyau[1,1]):
                s=1
            if(tab[i,j+1] == noyau[1,2]):
                s=1
                
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
    
    return tab2








def filtre_colonne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre colonne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 1 
            if(tab[i-1,j] != noyau[0,1]):
                s=0
            if(tab[i,j] != noyau[1,1]):
                s=0
            if(tab[i+1,j] != noyau[2,1]):
                s=0
    
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
                
    return tab2
       




def filtre_ligne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre ligne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 1 
            if(tab[i,j-1] != noyau[1,0]):
                s=0
            if(tab[i,j] != noyau[1,1]):
                s=0
            if(tab[i,j+1] != noyau[1,2]):
                s=0
    
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
    
    return tab2    
    

        
def filtre_ligne_colonne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes):
    #filtre ligne/colonne
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            s = 1 
            if(tab[i-1,j] != noyau[0,1]):
                s=0
            if(tab[i,j] != noyau[1,1]):
                s=0
            if(tab[i+1,j] != noyau[2,1]):
                s=0
            if(tab[i,j-1] != noyau[1,0]):
                s=0
            if(tab[i,j] != noyau[1,1]):
                s=0
            if(tab[i,j+1] != noyau[1,2]):
                s=0
                
            if(s == 0):        
                tab2[i,j] = 0
            else:
                tab2[i,j] = 255
    
    return tab2



def main():
    image = Image.open("EnrollementBDD/001_1_1.bmp")
    tab = np.array(image)
    tab2 = np.array(image)
    tab3 = np.array(image)                
    nb_lignes,nb_colonnes= tab.shape
    
    noyau = np.array([[255,255,255],
                      [255,255,255],
                      [255,255,255]])
    
    #####rendre l'image noir et blanc######      
    for i in range(1,nb_lignes-1):
        for j in range(1,nb_colonnes-1):
            if(tab[i,j]<100):
                tab[i,j]=0
            else:    
                tab[i,j]=255
    
            #####les differents filtres de dilatation#### 

    
    #tab2 = filtre_colonne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes)
    #tab2 = filtre_ligne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes)
    #tab2 = filtre_ligne_colonne_dilatation(tab,tab2,noyau,nb_lignes,nb_colonnes)
    
    
            ######les differents d'erosion#######
    
    #tab2 = filtre_colonne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes)
    #tab2 = filtre_ligne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes)
    #tab2 = filtre_ligne_colonne_erosion(tab,tab2,noyau,nb_lignes,nb_colonnes)
                
    




    Image.fromarray(tab2).show()
if __name__ == '__main__':
	main()