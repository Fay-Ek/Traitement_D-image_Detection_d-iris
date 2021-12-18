
import cv2
import numpy as np
from PIL import Image

def extraction_oeuil(img):
    im	= img.convert('RGB')
    planets = np.array(im)
    planets = planets[:, :, ::-1].copy() 
    
    gray_img=cv2.cvtColor(planets,	cv2.COLOR_BGR2GRAY)
    img	= cv2.medianBlur(gray_img,3)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    height,width = img.shape
    mask = np.zeros((height,width), np.uint8)
    
    #center
    
    counter = 0
    
    circles= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1200,param1=100,param2=20,minRadius=10,maxRadius=0)
    circles	= np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    
        # draw the center of the circle
        #cv2.circle(cimg,(i[0],i[1]),2,(0,0,0),3)
    
        # Draw on mask
        cv2.circle(mask,(i[0],i[1]),i[2],(255,255,255),-1)
        masked_data = cv2.bitwise_and(cimg, cimg, mask=mask)    
    
        # Apply Threshold
        _,thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)
    
        # Find Contour
        cnt = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    
        #print len(contours)
        x,y,w,h = cv2.boundingRect(cnt[0])
    
        # Crop masked_data
        crop = masked_data[y:y+h,x:x+w]
        
        
        # Write Files
        
        return Image.fromarray(crop)
        
     




