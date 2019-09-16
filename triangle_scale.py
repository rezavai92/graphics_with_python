import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter

img=np.zeros((250,250))

#Drawing a triangle
#points are (0,0), (1,1), (5,2)


P1 =(0,0)
P2= (1,1)
P3= (5,2)

#For better visibility in image, we took 20 times greater value of the respective co-ordinates
cv2.line(img,(P1[0]*20+100,P1[1]*20+100),(P3[0]* 20+100,P3[1]*20+100),(255,255,255))
cv2.line(img,(P1[0]*20+100,P1[1]*20+100),(P2[0]* 20+100,P2[1]*20+100),(255,255,255))
cv2.line(img,(P2[0]*20+100,P2[1]*20+100),(P3[0]* 20+100,P3[1]*20+100),(255,255,255))

# X

newPoint1=(-3,0)
newPoint2=(-5,-2)


cv2.line(img,(newPoint2[0]*20+100,newPoint2[1]*20+100),(P3[0]*20+100,P3[1]*20+100),(255,255,255))
cv2.line(img,(newPoint2[0]*20+100,newPoint2[1]*20+100),(newPoint1[0]*20+100,newPoint1[1]*20+100),(255,255,255))
cv2.line(img,(newPoint1[0]*20+100,newPoint1[1]*20+100),(P3[0]*20+100,P3[1]*20+100),(255,255,255))
cv2.imshow('img',img)
cv2.waitKey(0)
