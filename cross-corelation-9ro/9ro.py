from locale import normalize
import numpy as np
import cv2
from PIL import Image

def cc_trans(image, kernel):
    k_s = kernel.shape
    i_s = image.shape
    result = np.zeros((i_s[0] - k_s[0] + 1, i_s[1] - k_s[1] + 1, 3)) 
    for i in range(i_s[0] - k_s[0] + 1):
        for j in range(i_s[1] - k_s[1] + 1):
            result[i,j] = int(np.sum(image[i:i+k_s[0], j:j+k_s[1]]*kernel))
    return result

def normalize(img):
    m = np.amin(img)
    M = np.amax(img)
    return (img - m) / (M - m)


img = cv2.imread('9-ro.jpeg')
template = cv2.imread('template.png')
w,h = template.shape[1], template.shape[0]

# Normalize both image and template
nor_img = normalize(img)
nor_template = normalize(template)

# Calculate cross correlation between the img and template
cc_img = cc_trans(nor_img, nor_template)

# Normalize the cc img
cc_img = normalize(cc_img)
cc_img = 1 - cc_img

THRESHOLD = 0.98
loc = np.where(cc_img >= THRESHOLD)

f = set()

for y, x in sorted(zip(loc[0], loc[1])):
    # cv2.rectangle(cc_img, (x-w//2, y-h//2), (x + w//2, y + h//2), (0,0,255), 1)

    sensitivity = 100
    if (round(x/sensitivity), round(y/sensitivity)) not in f:
        cv2.rectangle(cc_img, (x-w//2, y-h//2), (x + w//2, y + h//2), (0,0,255), 1)
    f.add((round(x/sensitivity), round(y/sensitivity)))

    
    
    

print(f'Đây là lá bài {len(f)} rô')
cv2.imshow('cc_img',cc_img)
cv2.waitKey(0)