# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 04:30:30 2021

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
from building_k_mean import KMeans
from PIL import Image
#X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=42)
#X, y = make_blobs(centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40)
#print(X.shape)
def segmentation(R):
    tabR = np.array(R)
    
    Pixels = tabR.reshape((-1, 1))
    Pixels = np.float32(Pixels)
    
    k = KMeans(K=6, max_iters=5)
    y_pred = k.predict(Pixels)
    k.cent()
    y_pred = y_pred.astype(int)
    np.unique(y_pred)
    
    centers = np.uint8(k.cent())
    labels = y_pred.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(np.shape(R))
    
    return  Image.fromarray(segmented_image)
   