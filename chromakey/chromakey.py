import cv2 
import numpy as np
img=cv2.imread('chrome bg.jpg')
background=cv2.imread('backgroud.jpg')
img2= cv2.imread('chrome key.jpg')
background=cv2.resize(background,[img2.shape[1],img2.shape[0]])
print(background.shape)
print(img2.shape)

min_r= np.min(img[:,:,0])
min_g= np.min(img[:,:,1])
min_b= np.min(img[:,:,2])
max_r= np.max(img[:,:,0])
max_g= np.max(img[:,:,1])
max_b= np.max(img[:,:,2])
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if min_r < img2[i][j][0] and img2[i][j][0] < max_r and min_g < img2[i][j][1] and img2[i][j][1] < max_g and min_b < img2[i][j][2] and img2[i][j][2] < max_b :
            # img2[i][j][:] = [255,255,255]
            img2[i][j][:] = background[i][j][:]
# print(np.min(img))
# print(np.max(img))
cv2.imshow('img', img2)
cv2.waitKey(0)
