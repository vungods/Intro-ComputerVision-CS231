import cv2
import numpy as np
# image=np.array([[1,2,4,2],[1,3,2,2],[1,1,2,2]])
image=cv2.imread('lowconstract.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
unique, count=np.unique(image,return_counts=True)
print(unique,count)
cdf,hv=[],[]
sum=0
for i in range (0,len(unique)):
    sum+=count[i]
    cdf.append(sum)
for i in range (0,len(unique)):
    sum+=count[i]
    cdf.append(sum)
    hv.append(round((cdf[i]-cdf[0])/(image.shape[0]*image.shape[1]-cdf[0])*255))
xmax,ymax= np.shape(image)
for x in range (xmax):
    for y in range(ymax):
        for i in range (0,len(unique)):
                if image[x][y] == unique[i]:
                    image[x][y] = hv[i]
                    break
cv2.imshow('img',image)
cv2.waitKey(0)
