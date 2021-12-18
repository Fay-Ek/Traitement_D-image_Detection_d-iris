from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#image opening 
def histogram(img):
    
    size=img.size
    
    #jj total pixel number
    jj=size[0]*size[1]
    itc=np.zeros([256,3])
    #pixels
    x=np.zeros([jj])
    #calculer le nomber de chaque itencity
    o=0
    for i in range(size[0]):
        for j in range(size[1]):
            s=img.getpixel((i,j))
            itc[s,0]=itc[s,0]+1
            x[o]=s
            o=o+1
    #ploter l hitogram  etat 0
    print(np.amax(itc)  )
    #plt.hist(x, bins=255)
    #plt.show()
    l=0
    
    # claculer les probability de chaque itencity 
    for ii in range(256):
       l=itc[ii,0]+l
       itc[ii,1]=int(l)
       ll=int(l)/o*255
       ll=round(ll)
       itc[ii,2]=int(ll)
    
    #changer les valeurs des pixeles 
    for i in range(size[0]):
        for j in range(size[1]):
            ss=img.getpixel((i,j))
            img.putpixel((i,j),(int(itc[ss,2])))
    #ploter a nouveau l histograme pour les nouvelle valeur de pixels
    o=0
    for i in range(size[0]):
        for j in range(size[1]):
            s=img.getpixel((i,j))
            itc[s,0]=itc[s,0]+1
            x[o]=s
            o=o+1
    #ploter l hitogram
    print(np.amax(itc)  )
    #plt.hist(x, bins=255)
    #plt.show()
    #img.show()
    
    return img
