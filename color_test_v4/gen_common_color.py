import numpy as np
import cv2

pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\1\\'

with open('common_color.txt') as f:
    for line in f.readlines():
        sub = str(line).lower().split(',')[0]
        r = ''
        color_name = sub[:sub.index(' ')]
        print(color_name)
        for i in range(sub.index(' '), len(sub)):
            if sub[i] != ' ':
                r = sub[i:]
                break

        g = line.split(',')[1].strip()
        b = line.split(',')[2].strip()
        print(r, g, b)

        img = np.zeros([400, 400, 3], np.uint8)
        img[:, :, 0] = np.zeros([400, 400]) + int(b)
        img[:, :, 1] = np.zeros([400, 400]) + int(g)
        img[:, :, 2] = np.zeros([400, 400]) + int(r)

        cv2.imwrite(pic_dir + color_name + '.jpg', img)