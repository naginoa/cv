import numpy as np
import cv2

pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\1\\'
flag = 0
for i in range(1,255):
    if i>= 51:
        break
    img = np.zeros([400, 400, 3], np.uint8)
    flag = 0
    for b in range(1,260/5):
        for g in range(1,260/5):
            for r in range(1,260/5):
                img[:, :, 0] = np.zeros([400, 400]) + i*(b*5)
                img[:, :, 1] = np.zeros([400, 400]) + i*(g*5)
                img[:, :, 2] = np.zeros([400, 400]) + i*(r*5)
                print(i*(b*5))
                cv2.imwrite(pic_dir + str(flag)+'.jpg', img)
                flag += 1
            g+=5
        b+=5