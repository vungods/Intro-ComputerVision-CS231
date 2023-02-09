import cv2
import numpy as np

def cross_correlation_2D(img, ker):
    k=0
    convol = np.zeros((img.shape[0]-ker.shape[0]+1,img.shape[1]-ker.shape[1]+1))
    for i in range(ker.shape[1],img.shape[1]+1,1):
        h=0
        z = np.zeros((img.shape[0]-ker.shape[0]+1))
        for j in range(ker.shape[0],img.shape[0]+1,1):
            z[h]=sum(sum(img[k:i,h:j]*ker))
            h+=1
        convol[k]=z
        k+=1
    return convol
def convolution_2D(img,ker):
    ker = ker[::-1,::-1]
    return cross_correlation_2D(img,ker)

def cross_correlation_2D2(img,ker):
    result = np.zeros((img.shape[0] - ker.shape[0] + 1, img.shape[1] - ker.shape[1] + 1))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i, j] = np.sum(img[i:i+ker.shape[0], j:j+ker.shape[1]] * ker)
    return result
if __name__ == "__main__":
    img = np.array([[1,2,3,4,5,6,1],
    [4,5,6,73,6,4,1],[3,4,6,3,3,1,6],[3,45,3,5,4,1,6],[9,6,4,4,3,1,3],[12,4,3,1,5,4,3]
    ,[12,4,3,1,5,4,3]])
    ker = np.array([[1,0,0], [0,1,0], [0,0,1]])
    re_cross = cross_correlation_2D2(img,ker)
    print(re_cross)