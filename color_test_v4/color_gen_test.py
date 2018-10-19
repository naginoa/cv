import numpy as np
import cv2

pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\1\\'

img = np.zeros([400, 400, 3], np.uint8)
img[:, :, 0] = np.zeros([400, 400]) + 0
img[:, :, 1] = np.zeros([400, 400]) + 50
img[:, :, 2] = np.zeros([400, 400]) + 150
cv2.imwrite(pic_dir + str('test')+'.jpg', img)
