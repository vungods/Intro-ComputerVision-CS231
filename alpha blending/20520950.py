import cv2
import numpy as np
import imageio as im
fg=cv2.imread('vungo.jpg')
mask=cv2.imread('vungo.png')
print(mask.shape)
fg=cv2.resize(fg,(300,300))
mask=cv2.resize(mask,(300,300))
result_m=np.ones((300,300,4),dtype=int)
for i in range(0,mask.shape[0]):
    for j in range(0,mask.shape[1]):
        if mask[i,j,0]==mask[i,j,1]==mask[i,j,2]==255:
            result_m[i,j]=np.hstack((mask[i,j],[0]))
        else:
            result_m[i, j] = np.hstack((mask[i, j], [255]))
mask=result_m.copy()
print(mask.shape)
#url
url = "https://i.pinimg.com/originals/f9/6d/fb/f96dfb9f9d4e0b42af3888de8b9473a7.gif"
s_url ="https://c.tenor.com/0Fotn_LvJboAAAAC/smoke-burn.gif"

# url = "https://c.tenor.com/AaPeZRxwOuQAAAAC/fire-flames.gif"
frames = im.mimread(im.core.urlopen(url).read(), '.gif')
smokes= im.mimread(im.core.urlopen(s_url).read(), '.gif')

fg_h, fg_w, fg_c = fg.shape  
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h-fg_h)/2)
left = int((bg_w-fg_w)/2)

sm_h, sm_w, sm_c = smokes[0].shape
smtop = int((sm_h-fg_h)/2)
smleft = int((sm_w-fg_w)/2)
#Danh sach khung hinh cua background va smoke duoc crop bang kich thuoc foreground
bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]
smk = [sm[smtop: smtop + fg_h, smleft:smleft + fg_w, 0:3] for sm in smokes]
im.mimsave('smk.gif',smk)#dc 1 tap cac ảnh= 1 video
im.mimsave('bgs.gif',bgs)#dc 1 tap cac ảnh= 1 video

#lay tung khung hinh cua gif mang di tron
results = []
alpha = 0.8
for i in range(len(bgs)):
    result = fg.copy()
    result[mask[:,:,3] != 0] = alpha * result[mask[:,:,3] != 0]
    bgs[i][mask[:,:,3] != 0] = (1-alpha)*bgs[i][mask[:,:,3] != 0]
    bgs[i][mask[:,:,3] == 0] = (0.8) * smk[i][mask[:,:,3] == 0]  #them gia tri smoke vao vung 
    result = result + bgs[i]
    results.append(result)
    cv2.imshow('img',result)
    cv2.waitKey(10)
print(len(results))
print(results[0].shape)
im.mimsave('result.gif',results)


