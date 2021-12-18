# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 01:48:34 2021

@author: Lenovo
"""


import cv2 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np 
# read images
import math
def sift():
    #pourcentage des distance similaire cas de ressemblence
    super_pourcentage=0
    #pourcentage des distance similaire cas de non ressemblence
    lower_pourcentage=0
    resultt=False
    #message cas de non ressemblence
    result=""
    #message cas de non ressemblence
    resulttt=""
    opt=0
    img1 = cv2.imread("test.bmp", cv2.IMREAD_GRAYSCALE)
    r=1
    for i in range(1,10):
        for j in range(1,4):
            a=str(i)
            aa=str(j)
            rr=str(r)
            path = "EnrollementBDD2/00"+rr+"_1_"+aa+".bmp"
            img2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            height1, width1 = img1.shape
            height2, width2 = img2.shape
            # ORB Detector
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img2, None)
            #percent by which the image is resized
            width = 210
            height =210
            # dsize
            dsize = (width, height)
            
            # resize image
            img1 = cv2.resize(img1, dsize)
            img2 = cv2.resize(img2, dsize)
            
            
            # Brute Force Matching
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key = lambda x:x.distance)
            
            matching_result = cv2.drawMatches(img1, kp1, img2,kp2, matches[:20], None, flags=2)
             
            points1 = np.zeros((len(matches), 2), dtype=np.float32)  #Prints empty array of size equal to (matches, 2)
            points2 = np.zeros((len(matches), 2), dtype=np.float32)
            dist = np.zeros((len(matches), 1), dtype=np.float32)
            #boucle pour calcule Eclidien
            for i, match in enumerate(matches):
               points1[i, :] = kp1[match.queryIdx].pt    #gives index of the descriptor in the list of query descriptors
               points2[i, :] = kp2[match.trainIdx].pt    #gives index of the descriptor in the list of train descriptors
               # calcule Eclidien
               dist[i, 0]= math.sqrt((points2[i, 0] - points1[i, 0])**2 + (points2[i,1] - points1[i,1])**2)
            n, bins, patches = plt.hist(dist.flatten(), bins=range(256))
            indices = [i for i, x in enumerate(n) if x == max(n)]
            # de variable concern un intervale des distance similaire 
            intervalMIN=indices[0]-5
            intervalMAX=indices[0]+5
            #calculer le pourcentage des distance similaire par rapport au autre image
            point_similaire=0
            for i in range(intervalMIN,intervalMAX+1):
                point_similaire=point_similaire+n[i]
            pourcentage=point_similaire*100/len(matches)
            #souil d acceptation de ressemblence
            if pourcentage >35:
                if pourcentage > super_pourcentage:
                    matching_result_super=matching_result
                    resultt=True
                    opt=1
                    super_pourcentage=pourcentage
                    resulttt="Identification réussie \n avec un  matching : \n "+str(round(super_pourcentage))+"%"
            else:
                if lower_pourcentage<pourcentage:
                    matching_result_lower=matching_result
                    lower_pourcentage=pourcentage
                    result="Echec d'identification \n avec un matching : \n "+str(round(lower_pourcentage))+"%"
                    
        r=r+1
        
        
    if resultt==True:
        return Image.fromarray(matching_result_super),resulttt,opt
    else:
        return Image.fromarray(matching_result_lower),result,opt
