import cv2
import numpy as np
a , b, count = 7, -190, 0
stack = []
mat = np.zeros((200,200))
x_max, y_max = mat.shape[0], mat.shape[1]
# Generate 70% data
#x in range (0,200):

for x in range(0,y_max):
    y = a * x + b
    if y >= y_max:
        break
    elif y < 0:
        continue
    else:
        print(x,y)
        mat[x,y] = 1
        stack.append([x,y])
        count+=1
#Generate 30% data

print('(count*3)//7',(count*3)//7)
for x in range(0,(count*3)//7):
    x, y = np.random.random_integers(low=0, high=x_max-2, size=None), np.random.random_integers(low=0, high=y_max-2, size=None)
    if [x,y] not in stack:
        mat[int(x),int(y)]=1
        stack.append([x,y])
        print('bien x,y them vao')

    else: 
        print('bien x,y nam tren duong thang nen se khong them vao')
cv2.imshow('original image', mat)
cv2.waitKey(0)
