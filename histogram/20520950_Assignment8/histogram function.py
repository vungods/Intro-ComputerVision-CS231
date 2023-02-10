import cv2
import numpy as np
# image=np.array([[1,2,4,2],[1,3,2,2],[1,1,2,2]])
image=cv2.imread('lowconstract.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
unique,count = np.unique(image,return_counts=True)
cdf,hv=[],[]
sum=0
# for i in range(len(unique)):
#     sum+=count[i]
#     cdf.append(sum)
for i in range(len(unique)):
    sum+=count[i]
    cdf.append(sum)
    hv.append(round((cdf[i]-cdf[0])/(image.shape[0]*image.shape[1]-cdf[0])*255))
for i in range(len(unique)):
    image = np.where(image == unique[i], hv[i], image)
cv2.imshow('img',image)
cv2.waitKey(0)